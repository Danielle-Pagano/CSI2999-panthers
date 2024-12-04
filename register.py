import tkinter as tk
import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

class RegisterPage(tk.Frame):
    def __init__(self, parent, on_register_success):
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

        self.on_register_success = on_register_success

        # Set up register UI
        self.configure(bg="#000000")

        tk.Label(self, text="Register", bg="#000000", fg="white", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=20)
        tk.Label(self, text="First Name", bg="#000000", fg="white", font=("Arial", 15)).grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self, bg="#000000", fg="white")
        self.first_name_entry.grid(row=1, column=1, pady=10)

        tk.Label(self, text="Last Name", bg="#000000", fg="white", font=("Arial", 15)).grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self, bg="#000000", fg="white")
        self.last_name_entry.grid(row=2, column=1, pady=10)

        tk.Label(self, text="Email", bg="#000000", fg="white", font=("Arial", 15)).grid(row=3, column=0)
        self.email_entry = tk.Entry(self, bg="#000000", fg="white")
        self.email_entry.grid(row=3, column=1, pady=10)

        tk.Label(self, text="Password", bg="#000000", fg="white", font=("Arial", 15)).grid(row=4, column=0)
        self.password_entry = tk.Entry(self, show="*", bg="#000000", fg="white")
        self.password_entry.grid(row=4, column=1, pady=10)

        tk.Label(self, text="Pet Choice", bg="#000000", fg="white", font=("Arial", 15)).grid(row=5, column=0)
        self.pet_choice_var = tk.StringVar(self)
        self.pet_choice_var.set("Squirrel")
        tk.OptionMenu(self, self.pet_choice_var, "Squirrel", "Pigeon").grid(row=5, column=1, pady=10)

        tk.Label(self, text="Pet Name", bg="#000000", fg="white", font=("Arial", 15)).grid(row=6, column=0)
        self.pet_name_entry = tk.Entry(self, bg="#000000", fg="white")
        self.pet_name_entry.grid(row=6, column=1, pady=10)

        tk.Button(self, text="Register", bg="#000000", fg="black", command=self.register).grid(row=7, column=0, columnspan=2, pady=20)
        self.status_label = tk.Label(self, text="", bg="#000000", fg="red", font=("Arial", 12))
        self.status_label.grid(row=8, column=0, columnspan=2)

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        pet_choice = self.pet_choice_var.get().lower()
        pet_name = self.pet_name_entry.get()

        if not all([first_name, last_name, email, password, pet_choice, pet_name]):
            self.status_label.config(text="Please fill out all fields.", fg="red")
            return

        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db = self.firebase.database()
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "pet": {"type": pet_choice, "name": pet_name},
            }
            db.child("users").child(user_id).set(user_data)
            self.status_label.config(text="Registration Successful!", fg="green")
            self.on_register_success(user_data)
        except Exception as e:
            self.status_label.config(text=f"An error occurred: {str(e)}", fg="red")
