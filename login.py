import tkinter as tk

class LoginPage:
    def __init__(self, window, on_login_success, show_register_page):
        self.window = window
        self.window.configure(bg="#000000")  # Make the entire window black
        self.on_login_success = on_login_success
        self.show_register_page = show_register_page
        self.login_frame = tk.Frame(window, bg="#000000")

        # Login Label
        self.login_label = tk.Label(self.login_frame, text="Login", bg="#000000", font=("Arial", 30))
        self.login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

        # Username entry and label
        self.username_label = tk.Label(self.login_frame, text="Username", bg="#000000", font=("Arial", 15))
        self.username_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(self.login_frame, highlightthickness=0, bd=0, bg="#000000", fg="white")
        self.username_entry.grid(row=1, column=1, pady=10)

        # Password entry and label
        self.password_label = tk.Label(self.login_frame, text="Password", bg="#000000", font=("Arial", 15))
        self.password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*", highlightthickness=0, bd=0, bg="#000000", fg="white")
        self.password_entry.grid(row=2, column=1, pady=20)

        # Login button
        self.login_button = tk.Button(self.login_frame,
                                      text="Login",
                                      highlightthickness=0, 
                                      bd=0,
                                      bg="#000000", 
                                      relief="flat", 
                                      font=("Arial", 15),
                                      command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)

        #Register button
        self.register_button = tk.Button(self.login_frame,
                                      text="Register",
                                      highlightthickness=0, 
                                      bd=0,
                                      bg="#000000", 
                                      relief="flat", 
                                      font=("Arial", 15),
                                      command=self.show_register_page) 
        self.register_button.grid(row=4, column=0, columnspan=2, pady=30)


    def login(self):
        # Basic login logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "G" and password == "G":  # Placeholder validation
            self.on_login_success()  # Transition to the pet view
            print("Login successful")
        else:
            print("Login failed")

    def show(self):
        self.login_frame.pack()

    def hide(self):
        self.login_frame.pack_forget()
