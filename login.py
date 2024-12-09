import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from shared_firebase import db  # Shared Firebase database object

from register import display_image

from PIL import Image, ImageTk
import os


class LoginPage(ttk.Frame):
    def __init__(self, parent, on_login_success, show_register_page, controller):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.show_register_page = show_register_page
        self.controller = controller


class LoginPage(ttk.Frame):
    def __init__(self, parent, on_login_success, show_register_page):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.show_register_page = show_register_page

        self.configure(style="TFrame")  # Use default style

        # Create a custom style for labels with a white background and black text
        style = ttk.Style()
        style.configure("WhiteBgLabel.TLabel", background="white", foreground="black", font=("Arial", 15))

        # Login title
        ttk.Label(self, text="Login", font=("Arial", 30), style="WhiteBgLabel.TLabel").place(x=280, y=30)

        # Email field
        ttk.Label(self, text="Email", style="WhiteBgLabel.TLabel").place(x=230, y=100)
        self.email_entry = ttk.Entry(self, bootstyle="dark")
        self.email_entry.place(x=230,y=125, width=200)

        # Password field
        ttk.Label(self, text="Password", style="WhiteBgLabel.TLabel").place(x=230,y=175)
        self.password_entry = ttk.Entry(self, show="*", bootstyle="dark")
        self.password_entry.place(x=230,y=200, width=200)

        # Buttons
        ttk.Button(self, text="Login", bootstyle="primary", command=self.login).place(x=265,y=275)
        ttk.Button(self, text="Register", bootstyle="secondary", command=self.show_register_page).place(x=340,y=275)


        self.tb_size = (32, 32)
        self.home_icon = display_image("button_icons/home_icon.png", size=self.tb_size)
         
        ttk.Button(self,image=self.home_icon, bootstyle='secondary', command=lambda: self.controller.show_frame("HomeScreen")).place(x=15,y=365)

        # Status label
        self.login_status_label = ttk.Label(self, text="", font=("Arial", 12), bootstyle="danger")
        self.login_status_label.place(x=255,y=375)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            self.login_status_label.config(text="Both fields are required")
            return

        try:
            # Search for the user directly in the Firebase database
            users = db.child("users").get().val()
            if users:
                for user_id, user_data in users.items():
                    if user_data['email'] == email and user_data['password'] == password:  # Corrected key
                        self.on_login_success(user_data)
                        return
            self.login_status_label.config(text="Invalid email or password")
        except Exception as e:
            self.login_status_label.config(text=f"Error: {str(e)}")
