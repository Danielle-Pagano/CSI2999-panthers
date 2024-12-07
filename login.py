import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from shared_firebase import db  # Shared Firebase database object

class LoginPage(ttk.Frame):
    def __init__(self, parent, on_login_success, controller, show_register_page):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.show_register_page = show_register_page

        self.configure(style="TFrame")  # Use default style

        # Create a custom style for labels with a white background and black text
        style = ttk.Style()
        style.configure("WhiteBgLabel.TLabel", background="white", foreground="black", font=("Arial", 15))

        # Login title
        ttk.Label(self, text="Login", font=("Arial", 30), style="WhiteBgLabel.TLabel").grid(row=0, column=0, columnspan=2, pady=40)

        # Email field
        ttk.Label(self, text="Email", style="WhiteBgLabel.TLabel").grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(self, bootstyle="dark")
        self.email_entry.grid(row=1, column=1, pady=10)

        # Password field
        ttk.Label(self, text="Password", style="WhiteBgLabel.TLabel").grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self, show="*", bootstyle="dark")
        self.password_entry.grid(row=2, column=1, pady=20)

        # Buttons
        ttk.Button(self, text="Login", bootstyle="primary", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self, text="Register", bootstyle="secondary", command=self.show_register_page).grid(row=4, column=0, columnspan=2, pady=10)

        # Status label
        self.login_status_label = ttk.Label(self, text="", font=("Arial", 12), bootstyle="danger")
        self.login_status_label.grid(row=5, column=0, columnspan=2)

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
                        #############################################
                        #CALL TO NAVIGATE TO HOMESCREEN WITH PET TYPE
                        #############################################
                        self.controller.show_frame("MainScreen", pet_type=user_data['pet']['type'])
                        #############################################
                        #CALL TO NAVIGATE TO HOMESCREEN WITH PET TYPE
                        #############################################
                        return
            self.login_status_label.config(text="Invalid email or password")
        except Exception as e:
            self.login_status_label.config(text=f"Error: {str(e)}")
