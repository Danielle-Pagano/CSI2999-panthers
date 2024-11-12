# register.py
import tkinter as tk

class RegisterPage:
    def __init__(self, window, on_register_success):
        self.window = window
        self.on_register_success = on_register_success
        self.register_frame = tk.Frame(window, bg="#000000")

        # Register Label
        self.register_label = tk.Label(self.register_frame, text="Register", bg="#000000", fg="white", font=("Arial", 30))
        self.register_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

        # Username entry and label
        self.username_label = tk.Label(self.register_frame, text="Username", bg="#000000", fg="white", font=("Arial", 15))
        self.username_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(self.register_frame, highlightthickness=0, bd=0, bg="#000000", fg="white")
        self.username_entry.grid(row=1, column=1, pady=10)

        # Password entry and label
        self.password_label = tk.Label(self.register_frame, text="Password", bg="#000000", fg="white", font=("Arial", 15))
        self.password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(self.register_frame, show="*", highlightthickness=0, bd=0, bg="#000000", fg="white")
        self.password_entry.grid(row=2, column=1, pady=20)

        # Register button
        self.register_button = tk.Button(self.register_frame,
                                         text="Register",
                                         highlightthickness=0, 
                                         bd=0,
                                         bg="#000000", 
                                         fg="white",
                                         relief="flat", 
                                         font=("Arial", 15),
                                         command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=30)

    def register(self):
        # Placeholder for registration logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Registered username: {username}")
        self.on_register_success()  # Call back to main app after registration

    def show(self):
        self.register_frame.pack()

    def hide(self):
        self.register_frame.pack_forget()
