import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

firebase_config = {
    'apiKey': os.getenv("FIREBASE_API_KEY"),
    'authDomain': "petstkinter.firebaseapp.com",
    'projectId': "petstkinter",
    'databaseURL': os.getenv("FIREBASE_DATABASE_URL"),
    'storageBucket': "petstkinter.appspot.com",
    'messagingSenderId': "597279333277",
    'appId': "1:597279333277:web:5230058a7fc45fd0216d74"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
