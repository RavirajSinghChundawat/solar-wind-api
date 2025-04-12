#  Solar + Wind Predictive Maintenance API

This project is an end-to-end machine learning deployment of a **Predictive Maintenance System** for hybrid **solar and wind energy systems**. The system uses sensor data to detect potential failures in advance using an ML model, Flask API, and Power BI for real-time analytics.

---

##  Project Structure

```
Solarwind-api/
│
├── app/                             # Contains app.py for Flask API
│   └── app.py
│
├── predictive_maintenance_model.pkl  # Trained ML model
├── feature_scaler.pkl                # Fitted scaler object
├── requirements.txt                  # Python dependencies
├── runtime.txt                       # Python version for deployment
├── Procfile                          # For deployment on Render
├── README.md                         # Project Documentation (this file)
├── prediction_logs.csv               # (Auto-created on prediction)
```

---

##  Problem Statement

To predict whether a solar/wind system component is **healthy** or **faulty**, based on sensor readings like temperature, voltage, current, wind speed, solar irradiance, etc. Early detection improves performance, safety, and cost savings.

---

##  Model Details

- **Data**: Realistic Indian + global hybrid sensor data (`SolarWind_Hybrid_2025.csv`)
- **Algorithms**:
  - RandomForestClassifier (final deployed model with 96-98% accuracy)
  - GridSearchCV for hyperparameter tuning
- **Feature Engineering**:
  - Rolling Mean
  - Rate of Change
  - Time-based features
  - Anomaly Flags
- **Scaler**: StandardScaler

---

##  Prediction API (Flask)

The model is deployed using Flask and serves predictions via a `/predict` route.

###  API Endpoint

```
POST /predict
```

###  Input JSON Format

```json
{
  "features": [30.2, 12.5, 440.0, 3.5, 1010.5, ...]  # example feature values
}
```

###  Output JSON

```json
{
  "prediction": 1,
  "probability": 0.88
}
```

> `1` = Faulty | `0` = Healthy

---

##  Power BI Integration

Power BI is used to visualize:
- Live predictions
- Health status trends
- Device-wise fault ratio
- Timestamped prediction logs

###  Source:
The `prediction_logs.csv` file is auto-updated after every API call and can be imported into Power BI using a **Live Connection**.

---

##  Render Deployment Instructions

1. **Push this folder to GitHub**
2. Go to [Render.com](https://render.com)
3. New Web Service → Connect GitHub → Select repo
4. Set build and deploy commands:

```
Build command: pip install -r requirements.txt
Start command: gunicorn app:app
```

5. Add the following environment variables (if any)
6. Done! The app will be live with a public URL 🎉

---

## 🛠️ Setup for Local Testing

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app/app.py
```

---

##  Dependencies (requirements.txt)

```
Flask==2.2.5
numpy==1.24.3
joblib==1.3.2
gunicorn==21.2.0
scikit-learn==1.2.2
pandas==1.5.3
```

---

##  Files Explanation

| File/Folder           | Description                                      |
|----------------------|--------------------------------------------------|
| app/app.py           | Flask API for prediction                         |
| predictive_maintenance_model.pkl | Trained ML model                   |
| feature_scaler.pkl   | Standard Scaler object                           |
| requirements.txt     | Required Python libraries                        |
| Procfile             | Required by Render to start the web service      |
| runtime.txt          | Python version to be used (e.g., `python-3.11.11`)|
| prediction_logs.csv  | Live updated log file of predictions             |

---

##  Author

**Raviraj Singh**  
MSc Data Science and Analytics, Final Semester  
[LinkedIn](#) | [Medium](https://medium.com/@focusforge)

---

