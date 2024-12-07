import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import ttkbootstrap as tb
from PIL import Image, ImageTk
import os

import spriteFunctions as spf
import application
from Sprite_Stuff import SpriteSheetFramework as sprite
import threading, time

from Color_game import main as game

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

        # Background on home screen
        background_image = display_image("backgroundPic.jpg")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        semibold_font = import_custom_font("SemiBold.ttf", 30)
        title_label = tb.Label(self, text="Tomogatchi", anchor="n", font=semibold_font)
        title_label.pack(padx=10, pady=10)
        
        # # Separator
        # home_separator = ttk.Separator(self, orient='horizontal')
        # home_separator.pack(fill='x')
        
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
        # Initialize attributes
        self.petState = 0
        self.pet = sprite.Animal(0)  # Will be initialized later in update_user_info
        self.stop_animation = False  # Control flag for sprite animation
        self.is_busy = False  # Flag to indicate whether the pet is busy

        self.image_label = tk.Label(self)
        self.image_label.place(x=275, y=50)
        self.current_img = None

        threading.Thread(target=lambda: spf.sprite_animation(self)).start()

        # Happiness bar
        self.happiness_bar = tb.Progressbar(
            self,
            value=100,
            orient="horizontal",
            bootstyle="primary-striped",
            length=150,
            mode="determinate"
        )
        self.happiness_bar.place(x=475, y=270)

        self.happiness_label = tk.Label(
            self,
            text="Happiness",
            font=("Helvetica", 12)
        )
        self.happiness_label.place(x=475,y=245)

        # Hunger bar
        self.hunger_bar = tb.Progressbar(
            self,
            value=100,
            orient="horizontal",
            bootstyle="success-striped",
            length=150,
            mode="determinate"
        )
        self.hunger_bar.place(x=475, y=320)

        self.happiness_label = tk.Label(
            self,
            text="Hunger",
            font=("Helvetica", 12)
        )
        self.happiness_label.place(x=475,y=295)

        # Energy bar
        self.energy_bar = tb.Progressbar(
            self,
            value=100,
            orient="horizontal",
            bootstyle="warning-striped",
            length=150,
            mode="determinate"
        )
        self.energy_bar.place(x=475, y=370)

        self.happiness_label = tk.Label(
            self,
            text="Energy",
            font=("Helvetica", 12)
        )
        self.happiness_label.place(x=475,y=345)

        # Initialize progress bars
        self.initialize_progress_bars()

        # Load button icons
        self.tb_size = (48, 48)
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
            command=lambda:self.playGame(),
            cursor='hand2'
        ).place(x=25, y=258)

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
        ).place(x=110, y=332)

        # Home button at the bottom-left corner
        tb.Button(
            self,
            image=self.home_icon,
            bootstyle='secondary',
            command=self.homeButton,
            cursor='hand2'
        ).place(x=25, y=332)

        # Label for displaying user info (moved below buttons)
        self.user_label = tk.Label(
            self,
            text="",
            font=("Helvetica", 12),
            fg="white",
            bg="black",
            borderwidth=3,
            relief="solid",
            justify="center",
            anchor="center",
            padx=10,
            pady=10
        )
        self.user_label.place(x=200, y=275, width=250, height=75)

    def playGame(self):
        spf.trigger_animation_update(self, 1)
        threading.Thread(target=lambda: game.main()).start()

    def homeButton(self):
        def home():
            time.sleep(3)
            self.controller.show_frame("HomeScreen")
        spf.home_animation(self, 1)
        threading.Thread(target=home).start()

    def initialize_progress_bars(self):
        application.update_bar(self.happiness_bar, 100)
        application.update_bar(self.hunger_bar, 100)
        application.update_bar(self.energy_bar, 100)

    def update_user_info(self, user_data):
        # Extract user information
        first_name = user_data.get('first_name', 'Guest')
        last_name = user_data.get('last_name', '')
        pet_data = user_data.get('pet', {})
        pet_name = pet_data.get('name', 'Unknown')
        pet_type = pet_data.get('type', 'squirrel').lower()

        # Update user_label with styled and spaced text
        self.user_label.config(
            text=f"Welcome,\n{first_name} {last_name}\nPet: {pet_name}"
        )

        ####################################################
        # NEW LOGIC FOR CHOOSING PETS WHEN RREGISTERING
        ####################################################
        # Set pet type dynamically (0 for squirrel, 1 for pigeon)
        pet_type_index = 0 if pet_type == 'squirrel' else 1
        self.pet = sprite.Animal(pet_type_index)

        # Initialize pet animation if needed 
        ### This breaks the animation ###
        #if not self.stop_animation:
            #threading.Thread(target=lambda: spf.sprite_animation(self)).start()
        ####################################################
        # NEW LOGIC FOR CHOOSING PETS WHEN RREGISTERING
        ####################################################

# TomogatchiApp
class TomogatchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tomogatchi")
        self.resizable(False, False)
        self.geometry("650x425")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

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
