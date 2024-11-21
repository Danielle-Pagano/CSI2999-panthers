import tkinter as tk
import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

class RegisterPage:
    def __init__(self, window, on_register_success):
        firebaseConfig = {
            'apiKey': os.getenv("FIREBASE_API_KEY"),
            'authDomain': "petstkinter.firebaseapp.com",
            'projectId': "petstkinter",
            'databaseURL': os.getenv("FIREBASE_DATABASE_URL"),
            'storageBucket': "petstkinter.appspot.com",
            'messagingSenderId': "597279333277",
            'appId': "1:597279333277:web:5230058a7fc45fd0216d74"
        }

        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = self.firebase.auth()

        self.window = window
        self.on_register_success = on_register_success
        self.register_frame = tk.Frame(window, bg="#000000")

        # Register Label
        tk.Label(self.register_frame, text="Register", bg="#000000", fg="white", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=40)

        # Username entry and label
        tk.Label(self.register_frame, text="Username", bg="#000000", fg="white", font=("Arial", 15)).grid(row=1, column=0)
        self.username_entry = tk.Entry(self.register_frame, bg="#000000", fg="white")
        self.username_entry.grid(row=1, column=1, pady=10)

        # Password entry and label
        tk.Label(self.register_frame, text="Password", bg="#000000", fg="white", font=("Arial", 15)).grid(row=2, column=0)
        self.password_entry = tk.Entry(self.register_frame, show="*", bg="#000000", fg="white")
        self.password_entry.grid(row=2, column=1, pady=20)

        # Register button
        tk.Button(self.register_frame, text="Register", bg="#000000", fg="black", command=self.register).grid(row=3, column=0, columnspan=2, pady=30)

    def register(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.auth.create_user_with_email_and_password(email, password)
            print("Registration successful")
            self.on_register_success()
        except:
            print("Email already exists")

    def show(self):
        self.register_frame.pack()

    def hide(self):
        self.register_frame.pack_forget()