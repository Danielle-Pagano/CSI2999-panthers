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
        tk.Label(self.register_frame, text="Register", bg="#000000", fg="white", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=20)

        # First Name
        tk.Label(self.register_frame, text="First Name", bg="#000000", fg="white", font=("Arial", 15)).grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.register_frame, bg="#000000", fg="white")
        self.first_name_entry.grid(row=1, column=1, pady=10)

        # Last Name
        tk.Label(self.register_frame, text="Last Name", bg="#000000", fg="white", font=("Arial", 15)).grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.register_frame, bg="#000000", fg="white")
        self.last_name_entry.grid(row=2, column=1, pady=10)

        # Email
        tk.Label(self.register_frame, text="Email", bg="#000000", fg="white", font=("Arial", 15)).grid(row=3, column=0)
        self.email_entry = tk.Entry(self.register_frame, bg="#000000", fg="white")
        self.email_entry.grid(row=3, column=1, pady=10)

        # Password
        tk.Label(self.register_frame, text="Password", bg="#000000", fg="white", font=("Arial", 15)).grid(row=4, column=0)
        self.password_entry = tk.Entry(self.register_frame, show="*", bg="#000000", fg="white")
        self.password_entry.grid(row=4, column=1, pady=10)

        # Pet Choice Dropdown
        tk.Label(self.register_frame, text="Pet Choice", bg="#000000", fg="white", font=("Arial", 15)).grid(row=5, column=0)
        self.pet_choice_var = tk.StringVar(self.register_frame)
        self.pet_choice_var.set("Squirrel")  # Default value
        self.pet_choice_menu = tk.OptionMenu(self.register_frame, self.pet_choice_var, "Squirrel", "Pigeon")
        self.pet_choice_menu.config(bg="#000000", fg="white", font=("Arial", 12))
        self.pet_choice_menu.grid(row=5, column=1, pady=10)

        # Pet Name
        tk.Label(self.register_frame, text="Pet Name", bg="#000000", fg="white", font=("Arial", 15)).grid(row=6, column=0)
        self.pet_name_entry = tk.Entry(self.register_frame, bg="#000000", fg="white")
        self.pet_name_entry.grid(row=6, column=1, pady=10)

        # Register Button
        tk.Button(self.register_frame, text="Register", bg="#000000", fg="black", command=self.register).grid(row=7, column=0, columnspan=2, pady=20)

        # Status Label
        self.status_label = tk.Label(self.register_frame, text="", bg="#000000", fg="white", bd=0, highlightthickness=0, font=("Arial", 12))
        self.status_label.grid(row=8, column=0, columnspan=2, pady=10)

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        pet_choice = self.pet_choice_var.get().lower() 
        pet_name = self.pet_name_entry.get()

        # Check for empty fields
        if not all([first_name, last_name, email, password, pet_choice, pet_name]):
            self.status_label.config(text="Please fill out all fields.", fg="red")
            return

        try:
            # Firebase user creation
            user = self.auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']

            # Save additional user details
            db = self.firebase.database()
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "pet": {
                    "type": pet_choice,
                    "name": pet_name
                }
            }
            db.child("users").child(user_id).set(user_data)

            self.status_label.config(text="Registration Successful!", fg="green")
            self.on_register_success(user_data)
        except Exception as e:
            error_message = str(e)
            self.status_label.config(text=f"An error occurred: {error_message}", fg="red")

    def show(self):
        self.register_frame.pack()

    def hide(self):
        self.register_frame.pack_forget()
