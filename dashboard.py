import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://virtual-edge-ai-monitoring-default-rtdb.firebaseio.com/'
})

ref = db.reference('/anomalies')
data = ref.get()
df = pd.DataFrame(data.values()) if data else pd.DataFrame()

st.title("⚠️ Real-Time Anomaly Dashboard")
st.dataframe(df)
