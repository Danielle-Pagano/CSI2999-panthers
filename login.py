import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from shared_firebase import db  # Shared Firebase database object

from PIL import Image, ImageTk
import os

def display_image(filename, size=None):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images", filename)
    image = Image.open(image_path)
    if size:
        image = image.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

class RegisterPage(ttk.Frame):
    def __init__(self, parent, on_register_success, controller):
        super().__init__(parent)
        self.on_register_success = on_register_success
        self.controller = controller

        self.configure(style="TFrame")  # Use default style

        # Create a custom style for labels with white background and black text
        style = ttk.Style()
        style.configure("WhiteBgLabel.TLabel", background="white", foreground="black", font=("Arial", 12))

        # Register title
        ttk.Label(self, text="Register", font=("Arial", 30), style="WhiteBgLabel.TLabel").place(x=250, y=20)


        # First Name field
        ttk.Label(self, text="First Name", style="WhiteBgLabel.TLabel").place(x=175,y=100)
        self.first_name_entry = ttk.Entry(self, bootstyle="dark")
        self.first_name_entry.place(x=175,y=125)

        # Last Name field
        ttk.Label(self, text="Last Name", style="WhiteBgLabel.TLabel").place(x=350,y=100)
        self.last_name_entry = ttk.Entry(self, bootstyle="dark")
        self.last_name_entry.place(x=350,y=125)

        # Email field
        ttk.Label(self, text="Email", style="WhiteBgLabel.TLabel").place(x=100, y=175)
        self.username_entry = ttk.Entry(self, bootstyle="dark")
        self.username_entry.place(x=100, y=200)

        # Password field
        ttk.Label(self, text="Password", style="WhiteBgLabel.TLabel").place(x=250, y=175)
        self.password_entry = ttk.Entry(self, show="*", bootstyle="dark")
        self.password_entry.place(x=250, y=200)

        # Confirm password field
        ttk.Label(self, text="Confirm Password", style="WhiteBgLabel.TLabel").place(x=400, y=175)
        self.confirm_password_entry = ttk.Entry(self, show="*", bootstyle="dark")
        self.confirm_password_entry.place(x=400, y=200)

        # Pet name field
        ttk.Label(self, text="Pet Name", style="WhiteBgLabel.TLabel").place(x=175, y=250)
        self.pet_name_entry = ttk.Entry(self, bootstyle="dark")
        self.pet_name_entry.place(x=175, y=275)

        # Pet type dropdown
        ttk.Label(self, text="Pet Type", style="WhiteBgLabel.TLabel").place(x=350, y=250)
        self.pet_type_var = ttk.StringVar(value="Squirrel")
        ttk.Combobox(
            self,
            textvariable=self.pet_type_var,
            values=["Squirrel", "Pigeon"],
            bootstyle="dark"
        ).place(x=350, y=275)

        # Register button
        ttk.Button(self, text="Register", bootstyle="primary", command=self.register).place(x=290,y=325)

        self.tb_size = (32, 32)
        self.home_icon = display_image("button_icons/home_icon.png", size=self.tb_size)
        
        ttk.Button(self,image=self.home_icon, bootstyle='secondary', command=lambda: self.controller.show_frame("HomeScreen")).place(x=15,y=365)

        # Status label
        self.status_label = ttk.Label(self, text="", font=("Arial", 12), bootstyle="danger")
        self.status_label.place(x=250,y=375)

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        pet_name = self.pet_name_entry.get()
        pet_type = self.pet_type_var.get().lower()

        if not all([first_name, last_name, email, password, confirm_password, pet_name, pet_type]):
            self.status_label.config(text="Please fill out all fields.")
            return

        if password != confirm_password:
            self.status_label.config(text="Passwords do not match.")
            return

        try:
            # Add user directly to Firebase database
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "pet": {
                    "name": pet_name,
                    "type": pet_type,
                },
            }
            db.child("users").push(user_data)
            self.status_label.config(text="Registration successful!", bootstyle="success")
            self.on_register_success(user_data)
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

