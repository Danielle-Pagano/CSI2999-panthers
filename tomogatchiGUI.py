import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk
import tkinter.font as tkFont
from datetime import datetime
import os as os
import time
import threading

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

        tk.Label(signup_info_frame, text="* First Name").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(signup_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        
        tk.Label(signup_info_frame, text="* Last Name").grid(row=0, column=1)
        self.last_name_entry = tk.Entry(signup_info_frame)
        self.last_name_entry.grid(row=1, column=1)
        
        tk.Label(signup_info_frame, text="* Email").grid(row=0, column=2)
        self.email_entry = tk.Entry(signup_info_frame)
        self.email_entry.grid(row=1, column=2)

        tk.Label(signup_info_frame, text="Age").grid(row=2, column=0)
        self.age_entry = tk.Spinbox(signup_info_frame, from_=1, to=100)
        self.age_entry.grid(row=3, column=0)
        
        tk.Label(signup_info_frame, text="Birthday").grid(row=2, column=1)
        self.birthday_entry = tb.DateEntry(signup_info_frame, bootstyle="light")
        self.birthday_entry.grid(row=3, column=1)
        
        for widget in signup_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        animal_selection_frame = tk.LabelFrame(self, text="Animal")
        animal_selection_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

        tk.Label(animal_selection_frame, text="* Select Animal").grid(row=0, column=0)
        self.animal_entry = ttk.Combobox(animal_selection_frame, values=["Squirrel"])
        self.animal_entry.grid(row=1, column=0)
        
        tk.Label(animal_selection_frame, text="* Animal's Name").grid(row=0, column=2)
        self.animal_name_entry = tk.Entry(animal_selection_frame)
        self.animal_name_entry.grid(row=1, column=2)

        for widget in animal_selection_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        
        def valid_firstname():
            try:
                first_name = str(self.first_name_entry.get())
                return True
            except ValueError:
                return False
            
        def valid_lastname():
            try:
                last_name = str(self.last_name_entry.get())
                return True
            except ValueError:
                return False
        
        def valid_email():
            try:
                email = str(self.email_entry.get())
                if "@" and "." in email:
                    return True
                else:
                    return False
            except ValueError:
                return False

        def valid_age():
            try:
                age = int(self.age_entry.get())
                if age > 0:
                    return True
                else:
                    return False
            except ValueError:
                return False
            
        def valid_animal():
            try:
                animal = str(self.animal_entry.get())
                if animal.lower() == 'squirrel':
                    return True
                else:
                    return False
            except ValueError:
                return False


        def requirements_met():
            if (self.first_name_entry.get() == "" or self.last_name_entry.get() == "" or self.email_entry.get() == "" or self.animal_entry.get() == "" 
                or self.animal_name_entry.get() == "" or not valid_firstname() or not valid_lastname or not  valid_email() or not valid_animal() or not valid_age()):
               if not hasattr(self, 'error_message'):
                self.error_message = tk.Label(self, text="Please Fill all Required Fields", bg='#fff', fg='red')
                self.error_message.grid(row=2, column=0, sticky='n', pady=(5,0))
            else:
                
                if hasattr(self, 'error_message'):
                    self.error_message.grid_forget()
                
                first_name = self.first_name_entry.get()
                last_name = self.last_name_entry.get()
                email = self.email_entry.get()
                animal_name = self.animal_name_entry.get()
                animal = self.animal_entry.get()
                age = self.age_entry.get()                    
                #self.birthday_entry.bind("<<DateEntrySelected>>", self.birthday_entry.get_date())
                controller.show_frame("SaveFileScreen")

        tb.Button(self, text="Home", bootstyle='light', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=5, pady=5)
        
        tb.Button(self, text="Create Account", bootstyle='success', command=requirements_met,
                  cursor='hand2').grid(row=2, column=0, sticky='se', padx=5, pady=5)

#savefile screen frame
class SaveFileScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
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

        tb.Button(self, text="Home", bootstyle='light', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=5, pady=5)

class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        self.petState = 0
        self.pet = sprite.Animal(0)
        self.image_label = tk.Label(self)
        self.image_label.grid(row=0, column=1)
        self.current_img = None

        # Start the animation thread
        self.stop_animation = False
        self.is_busy = False
        threading.Thread(target=self.sprite_animation).start()

        # Setup GUI elements for activities (Play, Feed, etc.)
        self.setup_activity_buttons()

    def setup_activity_buttons(self):
        activity_buttons_frame = tk.LabelFrame(self, text="Activity")
        activity_buttons_frame.grid(row=1, column=1, padx=20, pady=(20, 10), sticky='n')
        tb.Button(activity_buttons_frame, text="Play", bootstyle='info',
                  command=lambda: self.trigger_animation_navigate(1), cursor='hand2').grid(row=0, column=0, sticky='ew')
        tb.Button(activity_buttons_frame, text="Feed", bootstyle='warning',
                  command=lambda: self.trigger_animation_navigate(2), cursor='hand2').grid(row=0, column=1, sticky='ew')
        tb.Button(activity_buttons_frame, text="Sleep", bootstyle='primary',
                  command=lambda: self.trigger_animation_navigate(3), cursor='hand2').grid(row=0, column=2, sticky='ew')
    
    def trigger_animation_navigate(self, state):
        self.petState = state
        self.is_busy = True

    def sprite_animation(self):
        # Run this in a loop to handle animation
        while not self.stop_animation:
            if self.is_busy:
                self.play_activity_animation()
                self.is_busy = False
                self.petState = 0  # Return to idle state
            else:
                self.play_idle_animation()

    def play_idle_animation(self):
        for frame_index in range(len(self.pet.frame[0])):  # Loop through idle frames
            if self.is_busy:
                break  # Interrupt idle if an activity is triggered
            self.update_sprite(0, frame_index)
            time.sleep(0.3)  # Control frame rate

    def play_activity_animation(self):
        for frame_index in range(len(self.pet.frame[self.petState])):  # Loop through activity frames
            self.update_sprite(self.petState, frame_index)
            time.sleep(0.3)  # Control frame rate

    def update_sprite(self, y, frame_index):
        # Retrieve and update the image for the current frame
        frame_image = self.pet.FrameGet(y, frame_index)
        self.current_img = ImageTk.PhotoImage(frame_image)
        self.image_label.config(image=self.current_img)

    def stop_animation(self):
        self.stop_animation = True


# not currently being used
class PlayScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        tb.Button(self, text="Home", bootstyle='light', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=20, pady=20)
        tb.Button(self, text="Back", bootstyle='secondary', command=lambda: controller.show_frame("MainScreen"),
                   cursor='hand2').grid(row=2, column=1, sticky='sw', padx=20, pady=20)


#not currently being used
class FeedScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        tb.Button(self, text="Home", bootstyle='light', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=20, pady=20)
        tb.Button(self, text="Back", bootstyle='secondary', command=lambda: controller.show_frame("MainScreen"),
                   cursor='hand2').grid(row=2, column=1, sticky='sw', padx=20, pady=20)

# not currently being used
class SleepScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky='nsew')

        tb.Button(self, text="Home", bootstyle='light', command=lambda: controller.show_frame("HomeScreen"),
                  cursor='hand2').grid(row=2, column=0, sticky='sw', padx=20, pady=20)
        tb.Button(self, text="Back", bootstyle='secondary', command=lambda: controller.show_frame("MainScreen"),
                   cursor='hand2').grid(row=2, column=1, sticky='sw', padx=20, pady=20)


class TomogatchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tomogatchi")
        self.resizable(False, False)
        
        self.frames = {}
        for FrameClass in (HomeScreen, SignUpScreen, SaveFileScreen, MainScreen, PlayScreen, FeedScreen, SleepScreen):
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
