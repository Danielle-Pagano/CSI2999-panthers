import tkinter as tk
import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

class LoginPage:
    def __init__(self, window, on_login_success, show_register_page):
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
        self.on_login_success = on_login_success
        self.show_register_page = show_register_page
        self.login_frame = tk.Frame(window, bg="#000000")

        # Login Label
        tk.Label(self.login_frame, text="Login", bg="#000000", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=40)

        # Username entry and label
        tk.Label(self.login_frame, text="Username", bg="#000000", font=("Arial", 15)).grid(row=1, column=0)
        self.username_entry = tk.Entry(self.login_frame, bg="#000000", fg="white")
        self.username_entry.grid(row=1, column=1, pady=10)

        # Password entry and label
        tk.Label(self.login_frame, text="Password", bg="#000000", font=("Arial", 15)).grid(row=2, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*", bg="#000000", fg="white")
        self.password_entry.grid(row=2, column=1, pady=20)

        # Login button
        tk.Button(self.login_frame, text="Login", bg="#000000", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)

        # Register button
        tk.Button(self.login_frame, text="Register", bg="#000000", command=self.show_register_page).grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.auth.sign_in_with_email_and_password(email, password)
            print("Login successful")
            self.on_login_success()
        except:
            print("Invalid email or password")

    def show(self):
        self.login_frame.pack()

    def hide(self):
        self.login_frame.pack_forget()