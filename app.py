 # app.py

from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import datetime
import os


# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("predictive_maintenance_model.joblib")
scaler = joblib.load("feature_scaler.joblib")

# Home Route
@app.route('/')
def home():
    return "Welcome to the Solar + Wind Predictive Maintenance API!"

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input JSON data
        data = request.get_json(force=True)
        
        # Extract feature values from JSON
        features = data['features']  # should be a list of values

        # Convert to NumPy array and reshape for model
        input_array = np.array(features).reshape(1, -1)

        # Scale the input
        input_scaled = scaler.transform(input_array)

        # Predict using the model
        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)

        result = {
            "prediction": int(prediction[0]),
            "probability": {
                "no_failure": round(prediction_proba[0][0]*100, 2),
                "failure": round(prediction_proba[0][1]*100, 2)
            }
        }
            # Logging prediction to CSV
        log_data = {
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'input': input_array.tolist(),
            'prediction': int(prediction[0]),
            'probability': round(prediction_proba[0][1], 4)
        }

        log_df = pd.DataFrame([log_data])

       # Check if CSV exists
        if os.path.exists("prediction_logs.csv"):
            log_df.to_csv("prediction_logs.csv", mode='a', header=False,index=False)
        else:
            log_df.to_csv("prediction_logs.csv", index=False)
        
        
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
