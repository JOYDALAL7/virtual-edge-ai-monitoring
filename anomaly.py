import pandas as pd

def detect_anomalies(df):
    """
    Simulate anomaly detection: return rows where 'value' > 90
    """
    anomalies = df[df['value'] > 90]
    return anomalies
