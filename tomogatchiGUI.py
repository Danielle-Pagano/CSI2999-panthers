import tkinter as tk
from tkinter import ttk

import ttkbootstrap as tb
from PIL import Image, ImageTk, ImageDraw, ImageFont

from tkinter.font import Font
import ttkbootstrap as tb

from PIL import Image, ImageTk, ImageFont
import os as os
import threading
from register import RegisterPage
from login import LoginPage

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

def import_custom_font(filename, font_size, text, text_color,bg_color):
    current_dir = os.path.dirname(__file__)
    font_path = os.path.join(current_dir, "fonts", filename)
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")


    font = ImageFont.truetype(font_path, font_size)
    temp_image = Image.new("RGBA", (1,1), "#655560")
    draw = ImageDraw.Draw(temp_image)
    text_bbox = draw.textbbox((0,0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0] + 10
    text_height = text_bbox[3] - text_bbox[1] + 10

    image = Image.new("RGBA", (text_width, text_height), "#655560")
    draw = ImageDraw.Draw(image)
    
    # Draw the text
    draw.text((5,5), text, font=font, fill=text_color)
    return ImageTk.PhotoImage(image)



    return Font(family="SemiBold.ttf", size=font_size)

# HomeScreen frame
class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        # Background on home screen

        self.background_size = (650,425)
        background_image = display_image("main_background.jpg", self.background_size)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image

        background_label.pack(fill="both", expand=True)
        
        #separates title screen from rest of frame
        home_separator = ttk.Separator(self, orient='horizontal')
        home_separator.pack(fill='x')
        
        login_button = tb.Button(self, text="LOGIN", bootstyle='success',
                                 command=lambda: controller.show_frame("LoginPage"), cursor='hand2')
        login_button.place(relx=0.4, rely=0.5, anchor='center')
        
        register_button = tb.Button(self, text="REGISTER", bootstyle='info',
                                  command=lambda: controller.show_frame("RegisterPage"), cursor='hand2')
        register_button.place(relx=0.6, rely=0.5, anchor='center')

#signup screen frame
class SignUpScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.place(relwidth=1, relheight=1) 
        
        signup_info_frame = tk.LabelFrame(self, text="User Information")
        signup_info_frame.place(x=20,y=20, relwidth=.9, height=150)

        tk.Label(signup_info_frame, text="First Name").place(x=50,y=10)
        self.first_name_entry = tk.Entry(signup_info_frame)
        self.first_name_entry.place(x=20, y=35)
        
        tk.Label(signup_info_frame, text="Last Name").place(x=210,y=10)
        self.last_name_entry = tk.Entry(signup_info_frame)
        self.last_name_entry.place(x=180, y=35)
        
        tk.Label(signup_info_frame, text="Email").place(x=385,y=10)
        self.email_entry = tk.Entry(signup_info_frame)
        self.email_entry.place(x=340,y=35)

        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        semibold_font = import_custom_font("SemiBold.ttf", 20, "Tomogatchi", "black", "#655560")
        title_label = tk.Label(self, image=semibold_font, bg='black')
        title_label.image = semibold_font
        title_label.pack(side="top", anchor="n", pady=0)
        
        # login_font = import_custom_font("SemiBold.ttf", 36, "Tomogatchi", "black", "white", )

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


        main_background = display_image("backgroundFrameMockup.jpg")
        main_background_label = tk.Label(self, image=main_background)
        main_background_label.image = main_background
        main_background_label.place(relx=0, rely=0,height=200, width=650)

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


class MainScreen(tk.Frame):
    def __init__(self, parent, controller,pet_type="squirrel"): #passed default value of squirrel
        super().__init__(parent)
        self.controller = controller
        self.place(relwidth=1, relheight=1) 

        ######################################################
        # Map pet types to indices
        ######################################################
        pet_type_mapping = {"squirrel": 0, "pigeon": 1}
        pet_index = pet_type_mapping.get(pet_type.lower(), 0)
        ######################################################
        # Map pet types to indices
        ######################################################

        # Setting up animation and label
        self.petState = 0
        self.pet = sprite.Animal(pet_index)  # Use pet_index based on chosen pet
        self.image_label = tk.Label(self)
        self.image_label.place(x=200, y=50)
        self.current_img = None

        #####################################################################################################
        #NAT'S ANIMATION AND LABEL INITIALIZATION (KEEP)
        #####################################################################################################
        '''
        # Setting up animation and label
        self.petState = 0
        self.pet = sprite.Animal(0) #This chooses the animal! currently takes 0 for squirrel or 1 for pidgeon
        self.image_label = tk.Label(self)
        self.image_label.place(x=200, y=50)
        self.current_img = None
        '''
        #####################################################################################################
        #NAT'S ANIMATION AND LABEL INITIALIZATION (KEEP)
        #####################################################################################################

        # Start the animation thread
        self.stop_animation = False
        self.is_busy = False

        ###################################################################
        #NAT'S THREADING LOGIC (KEEP)
        ###################################################################
        #threading.Thread(target=lambda: spf.sprite_animation(self)).start()
        ###################################################################
        #NAT'S THREADING LOGIC 
        ###################################################################

        ###################################################################
        #THREADING LOGIC THAT POSSIBLY FIXES ATTRUBUTE ERROR
        ###################################################################
        self.animation_thread = threading.Thread(target=lambda: spf.sprite_animation(self), daemon=True)
        self.after(100, self.animation_thread.start)
        ###################################################################
        #THREADING LOGIC THAT POSSIBLY FIXES ATTRUBUTE ERROR
        ###################################################################





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
            command=lambda:self.food_popup(50,200),
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


    def food_popup(self,x_position, y_position):
        food_frame = tk.Toplevel(self)
        food_frame.title("Choose Food")
        food_frame.geometry(f"200x100+{self.winfo_x() + x_position}+{self.winfo_y() + y_position}")

        food_frame.transient(self)  # Make the pop-up stay on top of the parent window
        food_frame.grab_set()
        
        self.food_size = (40,40)
        self.acorn_image = display_image("food_items/acorn.png", size=self.food_size)
        self.seed_image = display_image("food_items/seeds.png", size=self.food_size)

        style = ttk.Style()
        style.configure(
        "FoodButton.TButton", 
        borderwidth=0,  # Remove border
        background="white",  # Match background
        padding=0  # Remove padding around the image
        )

        
        ttk.Button(
            food_frame,
            image=self.acorn_image,
            cursor='hand2',
            style="FoodButton.TButton",
            command=lambda:self.feed_pet(food_frame)
            ).place(x=25,y=25)
        ttk.Button(
            food_frame, 
            image=self.seed_image, 
            cursor='hand2',
            style="FoodButton.TButton",
            command=lambda:self.feed_pet(food_frame)
            ).place(x=110,y=25)

    def feed_pet(self, popup):
        popup.destroy()
        spf.trigger_animation_update(self, 2)


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


        ##################################################################
        #LOGIC TO HANDLE LOGIN FORM
        ##################################################################
        # Function to handle successful LOGIN
        def handle_login_success(data):
            print("Login successful:", data)  # Replace with desired functionality
        ##################################################################
        #LOGIC TO HANDLE LOGIN FORM
        ################################################################## 

        ##################################################################
        #LOGIC TO HANDLE LOGIN FORM
        ##################################################################
        # Function to show the RegisterPage from LoginPage
        def show_register_page():
            self.show_frame("RegisterPage")
        ##################################################################
        #LOGIC TO HANDLE LOGIN FORM
        ##################################################################  
 

        ##################################################################
        #LOGIC TO HANDLE REGISTER FORM
        ##################################################################
        # Function to handle successful registration
        def handle_register_success(data):
            print("Registration successful:", data)  # Replace with desired functionality
        ##################################################################
        #LOGIC TO HANDLE REGISTER FORM
        ##################################################################    

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


        ##################################################################
        #LOGIC TO HANDLE REGISTER FORM
        ##################################################################
        # Add RegisterPage separately with its required argument
        register_frame = RegisterPage(self, self, handle_register_success)
        register_frame.controller = self  # Explicitly set the controller attribute
        self.frames["RegisterPage"] = register_frame
        register_frame.grid(row=0, column=0, sticky="nsew")
        ##################################################################
        #LOGIC  TO HANDLE REGISTER FORM
        ##################################################################

        ##################################################################
        #LOGIC TO HANDLE REGISTER FORM
        ##################################################################
        # Add RegisterPage separately with its required argument
        login_frame = LoginPage(self, handle_login_success, self, show_register_page)
        self.frames["LoginPage"] = login_frame
        login_frame.controller = self
        login_frame.grid(row=0, column=0, sticky="nsew")
        ##################################################################
        #LOGIC  TO HANDLE REGISTER FORM
        ##################################################################
        

        # Add LoginPage and RegisterPage

        self.frames["LoginPage"] = LoginPage(self, self.on_login_success, self.show_register_page, self)
        self.frames["RegisterPage"] = RegisterPage(self, self.on_register_success, self)

        self.frames["LoginPage"] = LoginPage(self, self.on_login_success, self.show_register_page)
        self.frames["RegisterPage"] = RegisterPage(self, self.on_register_success)
        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["RegisterPage"].grid(row=0, column=0, sticky="nsew")

        # Start with HomeScreen

        self.show_frame("HomeScreen")
    


    def show_frame(self, frame_name, pet_type=None):
        frame = self.frames[frame_name]
        if frame_name == "MainScreen" and pet_type:
                frame.pet = sprite.Animal({"squirrel": 0, "pigeon": 1}.get(pet_type.lower(), 0))
        frame.tkraise()

    ###################################
    #NATS SHOW FRAME LOGIC
    ##################################
    '''

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
    '''
    ###################################
    #NATS SHOW FRAME LOGIC
    ##################################

    ###################################################################
    #THREADING LOGIC THAT POSSIBLY FIXES ATTRUBUTE ERROR
    ###################################################################
    def destroy(self):
        # Notify MainScreen to stop the animation
        if "MainScreen" in self.frames:
            self.frames["MainScreen"].stop_animation = True
        super().destroy() 
    ###################################################################
    #THREADING LOGIC THAT POSSIBLY FIXES ATTRUBUTE ERROR
    ###################################################################


if __name__ == "__main__":
    app = TomogatchiApp()
    app.mainloop()
