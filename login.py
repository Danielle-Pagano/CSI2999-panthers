import tkinter as tk
import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

class LoginPage(tk.Frame):
    def __init__(self, parent, on_login_success, show_register_page):
        super().__init__(parent)
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

        self.on_login_success = on_login_success
        self.show_register_page = show_register_page

        # Set up login UI
        self.configure(bg="#000000")

        # Login Label
        tk.Label(self, text="Login", bg="#000000", font=("Arial", 30), fg="white").grid(row=0, column=0, columnspan=2, pady=40)

        # Username entry and label
        tk.Label(self, text="Username", bg="#000000", font=("Arial", 15), fg="white").grid(row=1, column=0)
        self.username_entry = tk.Entry(self, bg="#000000", fg="white")
        self.username_entry.grid(row=1, column=1, pady=10)

        # Password entry and label
        tk.Label(self, text="Password", bg="#000000", font=("Arial", 15), fg="white").grid(row=2, column=0)
        self.password_entry = tk.Entry(self, show="*", bg="#000000", fg="white")
        self.password_entry.grid(row=2, column=1, pady=20)

        # Login button
        tk.Button(self, text="Login", bg="#000000", fg="black", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)

        # Register button
        tk.Button(self, text="Register", bg="#000000", fg="black", command=self.show_register_page).grid(row=4, column=0, columnspan=2, pady=10)

        # Login Status label
        self.login_status_label = tk.Label(self, text="", bg="#000000", font=("Arial", 12), fg="red")
        self.login_status_label.grid(row=5, column=0, columnspan=2)

    def login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            self.login_status_label.config(text="Both fields are required", fg="red")
            return

        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']
            db = self.firebase.database()
            user_data = db.child("users").child(user_id).get().val()

            if user_data:
                self.on_login_success(user_data)
            else:
                self.login_status_label.config(text="User data not found", fg="red")
        except Exception:
            self.login_status_label.config(text="Invalid email or password", fg="red")
