import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import ttkbootstrap as tb
from PIL import Image, ImageTk
import os
import spriteFunctions as spf
import application
from Sprite_Stuff import SpriteSheetFramework as sprite
from login import LoginPage
from register import RegisterPage

cd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# for displaying image on screen with universal file path
def display_image(filename, size=None):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images", filename)
    image = Image.open(image_path)
    if size:
        image = image.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

def import_custom_font(filename, font_size):
    current_dir = os.path.dirname(__file__)
    font_path = os.path.join(current_dir, "fonts", filename)
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")
    return Font(family="SemiBold.ttf", size=font_size)

# HomeScreen frame
class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        semibold_font = import_custom_font("SemiBold.ttf", 30)
        title_label = tb.Label(self, text="Tomogatchi", anchor="n", font=semibold_font)
        title_label.pack(padx=10, pady=10)

        # Background on home screen
        background_image = display_image("backgroundPic.jpg")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.pack(fill="both", expand=True)
        
        # Separator
        home_separator = ttk.Separator(self, orient='horizontal')
        home_separator.pack(fill='x')
        
        # Login Button
        login_button = tb.Button(
            self, text="Login", bootstyle='success',
            command=lambda: controller.show_frame("LoginPage"), cursor='hand2'
        )
        login_button.place(relx=0.4, rely=0.5, anchor='center')
        
        # Register Button
        register_button = tb.Button(
            self, text="Register", bootstyle='info',
            command=lambda: controller.show_frame("RegisterPage"), cursor='hand2'
        )
        register_button.place(relx=0.6, rely=0.5, anchor='center')

# MainScreen frame
class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.place(relwidth=1, relheight=1)

        # Label for displaying user info
        self.user_label = tk.Label(self, text="", font=("Helvetica", 15))
        self.user_label.place(x=20, y=20)

        # Setting up animation attributes
        self.petState = 0
        self.pet = sprite.Animal(0)  # Choose the animal (0 for squirrel, 1 for pigeon)
        self.image_label = tk.Label(self)
        self.image_label.place(x=200, y=50)
        self.current_img = None

        # Initialize animation control flags
        self.stop_animation = False  # Control flag for sprite animation
        self.is_busy = False  # Flag to indicate whether the pet is busy

        # Start the animation with after
        self.animate()

        # Load button icons
        self.tb_size = (42, 42)
        self.sleep_icon = display_image("button_icons/sleep_button.png", size=self.tb_size)
        self.eat_icon = display_image("button_icons/eat_button.png", size=self.tb_size)
        self.play_icon = display_image("button_icons/play_button.png", size=self.tb_size)
        self.home_icon = display_image("button_icons/home_icon.png", size=self.tb_size)

        # Menu Label
        self.menu_label = tk.Label(self, text="Menu", font=('Helvetica', 15), borderwidth=2, relief="solid")
        self.menu_label.place(relwidth=1, x=0, y=200, height=40)

        # Buttons inside the activity frame
        tb.Button(  # Play
            self,
            image=self.play_icon,
            bootstyle="primary",
            command=lambda: spf.trigger_animation_update(self, 1),
            cursor='hand2'
        ).place(x=35, y=258)

        tb.Button(  # Eat
            self,
            image=self.eat_icon,
            bootstyle="success",
            command=lambda: spf.trigger_animation_update(self, 2),
            cursor='hand2'
        ).place(x=110, y=258)

        tb.Button(  # Sleep
            self,
            image=self.sleep_icon,
            bootstyle="warning",
            command=lambda: spf.trigger_animation_update(self, 3),
            cursor='hand2'
        ).place(x=110, y=322)

        # Home button at the bottom-left corner
        tb.Button(
            self,
            image=self.home_icon,
            bootstyle='secondary',
            command=lambda: controller.show_frame("HomeScreen"),
            cursor='hand2'
        ).place(x=35, y=322)

        # Initialize animations after rendering
        self.after(500, self.animate)

    def animate(self):
        print("Animating...")
        spf.sprite_animation(self)  # Call sprite animation
        if not self.stop_animation:
            self.after(5000000000, self.animate)  # Schedule the next animation cycle

    def update_user_info(self, user_data):
    # Handle missing fields gracefully
        first_name = user_data.get('first_name', 'Guest')
        last_name = user_data.get('last_name', '')
        pet_name = user_data.get('pet', {}).get('name', 'Unknown')
    
        self.user_label.config(
            text=f"Welcome, {first_name} {last_name}!\nYour pet: {pet_name}"
        )

# TomogatchiApp
class TomogatchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tomogatchi")
        self.resizable(False, False)

        # Initialize user data
        self.user_data = None
        
        self.frames = {}
        for FrameClass in (HomeScreen, MainScreen):
            frame = FrameClass(self, self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Add LoginPage and RegisterPage
        self.frames["LoginPage"] = LoginPage(self, self.on_login_success, self.show_register_page)
        self.frames["RegisterPage"] = RegisterPage(self, self.on_register_success)
        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["RegisterPage"].grid(row=0, column=0, sticky="nsew")

        # Start with HomeScreen
        self.show_frame("HomeScreen")

    def on_login_success(self, user_data):
        print("Login successful, transitioning to MainScreen")
        self.user_data = user_data
        self.frames["MainScreen"].update_user_info(user_data)
        self.show_frame("MainScreen")

    def on_register_success(self, user_data):
        print("Registration successful, transitioning to MainScreen")
        self.user_data = user_data
        self.frames["MainScreen"].update_user_info(user_data)
        self.show_frame("MainScreen")

    def show_register_page(self):
        print("Navigating to RegisterPage")
        self.show_frame("RegisterPage")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

if __name__ == "__main__":
    app = TomogatchiApp()
    app.mainloop()
