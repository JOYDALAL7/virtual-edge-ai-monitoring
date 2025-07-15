import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://virtual-edge-ai-monitoring-default-rtdb.firebaseio.com/'
})

def send_to_firebase(data):
    ref = db.reference('/anomalies')
    ref.push(data)
