import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk
import os as os
import time, threading

from Sprite_Stuff import spriteFunctions as spf
import app, accountCreation
from Sprite_Stuff import SpriteSheetFramework as sprite

cd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# for displaying image on screen with universal file path
def display_image(filename):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images", filename)
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    return photo


#HomeScreen frame
class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')
        
        title_label = tb.Label(self, text="Welcome!", anchor="n", font=('Arial', 30))
        title_label.pack(padx=10, pady=10)

        # background on home screen
        background_image = display_image("backgroundPic.jpg")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.pack(fill="both", expand=True)
        
        #separates title screen from rest of frame
        home_separator = ttk.Separator(self, orient='horizontal')
        home_separator.pack(fill='x')
        
        start_button = tb.Button(self, text="START", bootstyle='success',
                                 command=lambda: controller.show_frame("SaveFileScreen"), cursor='hand2')
        start_button.place(relx=0.4, rely=0.5, anchor='center')
        
        signup_button = tb.Button(self, text="SIGN UP", bootstyle='info',
                                  command=lambda: controller.show_frame("SignUpScreen"), cursor='hand2')
        signup_button.place(relx=0.6, rely=0.5, anchor='center')

#signup screen frame
class SignUpScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')
        
        signup_info_frame = tk.LabelFrame(self, text="User Information")
        signup_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        tk.Label(signup_info_frame, text="First Name").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(signup_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        
        tk.Label(signup_info_frame, text="Last Name").grid(row=0, column=1)
        self.last_name_entry = tk.Entry(signup_info_frame)
        self.last_name_entry.grid(row=1, column=1)
        
        tk.Label(signup_info_frame, text="Email").grid(row=0, column=2)
        self.email_entry = tk.Entry(signup_info_frame)
        self.email_entry.grid(row=1, column=2)

        tk.Label(signup_info_frame, text="Age").grid(row=2, column=0)
        self.age_entry = tk.Spinbox(signup_info_frame, from_=1, to=100)
        self.age_entry.grid(row=3, column=0)
        
        tk.Label(signup_info_frame, text="Password").grid(row=2, column=1)
        self.password_entry = tk.Entry(signup_info_frame)
        self.password_entry.grid(row=3, column=1)
        
        for widget in signup_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        animal_selection_frame = tk.LabelFrame(self, text="Animal")
        animal_selection_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

        tk.Label(animal_selection_frame, text="Select Animal").grid(row=0, column=0)
        self.animal_entry = ttk.Combobox(animal_selection_frame, values=["Squirrel"])
        self.animal_entry.grid(row=1, column=0)
        
        tk.Label(animal_selection_frame, text="Animal's Name").grid(row=0, column=2)
        self.animal_name_entry = tk.Entry(animal_selection_frame)
        self.animal_name_entry.grid(row=1, column=2)

        for widget in animal_selection_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        
        accountCreation.valid_firstname(self.first_name_entry)
        accountCreation.valid_lastname(self.last_name_entry)
        accountCreation.valid_password(self.password_entry)
        accountCreation.valid_email(self.email_entry)
        accountCreation.valid_age(self.age_entry)
        accountCreation.valid_animal(self.animal_entry)
        accountCreation.valid_animal_name(self.animal_name_entry)
        accountCreation.valid_requirements(self.first_name_entry, self.last_name_entry, self.password_entry, self.email_entry, self.animal_entry, self.animal_name_entry, self.age_entry)

        tb.Button(self, text="Home", bootstyle='light', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=5, pady=5)
        
        tb.Button(self, text="Create Account", bootstyle='success', command = lambda: accountCreation.requirements_met(self, controller, self.first_name_entry, self.last_name_entry,
                    self.password_entry, self.email_entry, self.animal_entry, self.animal_name_entry, self.age_entry),
                  cursor='hand2').grid(row=2, column=0, sticky='se', padx=5, pady=5)

#savefile screen frame
class SaveFileScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.rowconfigure(0)
        self.rowconfigure(1)
        self.rowconfigure(2)
        self.columnconfigure(0)

        self.grid(row=0, column=0, sticky='nsew')

        #currently place holder
        continue_file_frame = tk.LabelFrame(self, text="Save File 1")
        continue_file_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        tb.Button(continue_file_frame, text="Continue", bootstyle='success',
                  command=lambda: controller.show_frame("MainScreen"), cursor='hand2').grid(row=0, column=0, sticky='ew')
        
        tb.Button(continue_file_frame, text="Delete Save", bootstyle='danger', cursor='hand2').grid(row=1, column=0, sticky='ew')
        
        tk.Label(continue_file_frame, text="Animal Name").grid(row=0, column=1)
        tk.Label(continue_file_frame, text="Time Spent").grid(row=1, column=1)

        new_save_frame = tk.LabelFrame(self, text="New Save File")
        new_save_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        
        tb.Button(new_save_frame, text="New File", bootstyle='secondary',
                  command=lambda: controller.show_frame("MainScreen"), cursor="hand2").grid(row=0, column=0, sticky='ew')
        
        tk.Label(new_save_frame, text="______").grid(row=0, column=1)
        tk.Label(new_save_frame, text="______").grid(row=1, column=1)

        tb.Button(self, text="Home", bootstyle='secondary', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=5, pady=5)

class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.petState = 0
        self.pet = sprite.Animal(0)
        self.image_label = tk.Label(self)
        self.image_label.grid(row=0, column=0, rowspan=3, sticky="nsw", padx=10, pady=10)
        self.current_img = None

        # Start the animation thread
        self.stop_animation = False
        self.is_busy = False
        threading.Thread(target = lambda: spf.sprite_animation(self)).start()

        # Setup GUI elements for activities (Play, Feed, Sleep)
        activity_buttons_frame = tk.LabelFrame(self, text="Activity")
        activity_buttons_frame.grid(row=2, column=2, padx=20, pady=(20, 10), sticky='se')
        tb.Button(activity_buttons_frame, text="Play", bootstyle='info',
                  command=lambda: spf.trigger_animation_update(self, 1), cursor='hand2').grid(row=0, column=0, sticky='ew')
        tb.Button(activity_buttons_frame, text="Feed", bootstyle='warning',
                  command=lambda: spf.trigger_animation_update(self, 2), cursor='hand2').grid(row=0, column=1, sticky='ew')
        tb.Button(activity_buttons_frame, text="Sleep", bootstyle='primary',
                  command=lambda: spf.trigger_animation_update(self, 3), cursor='hand2').grid(row=0, column=2, sticky='ew')
        
        # Progress Bars for Animal Statistics
        health_bars_label = tk.LabelFrame(self, text="Health")
        health_bars_label.grid(row=0, column=2, sticky='ne', padx=10, pady=10)
        # 100 seconds for countdown time to run out
        self.countdown_time = 100

        #creates happiness bar
        self.happiness_bar = ttk.Progressbar(health_bars_label, value = 100, style = "info.Striped.TProgressbar", orient="horizontal", length = 200, mode = 'determinate')
        self.happiness_bar.grid(row=1, column=0, padx=10, pady=5, sticky= 'ne')
        tk.Label(health_bars_label, text="Happiness").grid(row=0, column=0,padx=10, pady=5, sticky= 'ew')
        #progress bar starts off full (value of countdown time)
        self.happiness_bar["maximum"] = self.countdown_time
        self.happiness_bar["value"] = self.countdown_time
        app.update_happiness_bar(self.happiness_bar, self.countdown_time)

        self.hunger_bar = ttk.Progressbar(health_bars_label, value = 100, style = "warning.Striped.TProgressbar", orient="horizontal", length=200, mode = 'determinate')
        self.hunger_bar.grid(row=3, column=0, padx=10, pady=5, sticky='ew')
        tk.Label(health_bars_label, text="Hunger").grid(row=2, column=0,padx=10, pady=5, sticky='ew')
        self.hunger_bar["maximum"] = self.countdown_time
        self.hunger_bar["value"] = self.countdown_time
        app.update_hunger_bar(self.hunger_bar, self.countdown_time)

        self.energy_bar = ttk.Progressbar(health_bars_label,value = 100, style = "primary.Striped.TProgressbar", orient="horizontal", length = 200, mode = 'determinate')
        self.energy_bar.grid(row=5, column=0, padx=10, pady=5, sticky='ew')
        tk.Label(health_bars_label, text='Energy').grid(row=4, column=0, padx=10, pady=5, sticky='ew')
        self.energy_bar["maximum"] = self.countdown_time
        self.energy_bar["value"] = self.countdown_time
        app.update_energy_bar(self.energy_bar, self.countdown_time)

        tb.Button(self, text="Home", bootstyle='secondary', 
                                command=lambda: controller.show_frame("HomeScreen"), cursor='hand2').grid(row=2, column=0, padx=10, pady=10, sticky='sw')
    

class TomogatchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tomogatchi")
        self.resizable(False, False)
        
        self.frames = {}
        for FrameClass in (HomeScreen, SignUpScreen, SaveFileScreen, MainScreen):
            frame = FrameClass(self, self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomeScreen")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

if __name__ == "__main__":
    app = TomogatchiApp()
    app.mainloop()
