import pandas as pd
from anomaly import detect_anomalies
from firebase_utils import send_to_firebase

df = pd.read_csv("sensor_data.csv")
result = detect_anomalies(df)
send_to_firebase(result.to_dict(orient="records"))
