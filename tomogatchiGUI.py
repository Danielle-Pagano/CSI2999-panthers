import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os as os

# Importing sprite framework
from Sprite_Stuff import SpriteSheetFramework as sprite
# Dynamic File Path (Will read where this python file is running and output a string)
cd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#print (cd)

#A function will need to set adoptedAnimal's Value
adoptedAnimal = 0
pet = sprite.Animal(adoptedAnimal)


root = tb.Window(themename='morph')
root.rowconfigure(0)
root.columnconfigure(0)

# frame set ups
homescreen = tk.Frame(root)
signup = tk.Frame(root)
savefile = tk.Frame(root)
mainscreen = tk.Frame(root)

# frame grids
homescreen.grid(row=0, column=0, sticky='nsew')
signup.grid(row=0, column=0, sticky="nsew")
savefile.grid(row=0, column=0, sticky="nsew")
mainscreen.grid(row=0, column=0, sticky="nsew")

#cannot get this to work right now

#background=Image.open("images/backgroundPic.jpeg")
#background=ImageTk.PhotoImage(background)
#image_label=tk.Label(homescreen,image=background)
#image_label.pack(pady=20)

homescreen.rowconfigure(0)
homescreen.columnconfigure(0)

title_label=tb.Label(homescreen, text="Welcome!",anchor=N, font=('Arial',30))
title_label.pack(padx=10,pady=10)

# creates line beneath title
home_separator=ttk.Separator(homescreen, orient='horizontal')
home_separator.pack(fill='x')

# need to have log in feature/frame
start_button=tb.Button(homescreen, text="START", bootstyle='success',command=lambda: savefile.tkraise(), cursor='hand2')
start_button.place(relx=.4,rely=.5, anchor='center')

# goes to sign up frame
signup_button=tb.Button(homescreen, text="SIGN UP", bootstyle='info', command=lambda: signup.tkraise(), cursor='hand2')
signup_button.place(relx=.6,rely=.5,anchor='center')


signup.rowconfigure(0, weight=1)
signup.columnconfigure(0, weight=1)

# label frame with user information
# entry widgets don't do anything yet
signup_info_frame = tk.LabelFrame(signup, text="User Information")
signup_info_frame.grid(row=0,column=0, padx=20, pady=20,sticky='nsew')

first_name = tk.Label(signup_info_frame, text="First Name")
first_name.grid(row=0, column=0)

last_name = tk.Label(signup_info_frame, text="Last Name")
last_name.grid(row=0, column=1)

first_name_entry = tk.Entry(signup_info_frame)
last_name_entry = tk.Entry(signup_info_frame)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

email = tk.Label(signup_info_frame,text="Email")
email.grid(row=0, column=2)

email_entry = tk.Entry(signup_info_frame)
email_entry.grid(row=1, column=2)

# can enter manually as well
age_label = tk.Label(signup_info_frame, text="Age")
age_spinbox=tk.Spinbox(signup_info_frame, from_=1, to=100)

age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

# can enter manually as well
birthday_label=tk.Label(signup_info_frame, text="Birthday")
birthday_label.grid(row=2, column=1)

birthday_entry=tb.DateEntry(signup_info_frame,bootstyle="light")
birthday_entry.grid(row=3,column=1)

for widget in signup_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# drop down only contains squirrel at the moment
animal_selection_frame=tk.LabelFrame(signup, text="Animal")
animal_selection_frame.grid(row=1,column=0, sticky="news", padx=20, pady=20)

# name will be saved moving forward
select_animal=tk.Label(animal_selection_frame, text="Select Animal")
select_animal.grid(row=0, column=0)

animal_chosen=ttk.Combobox(animal_selection_frame, values = ["Squirrel"])
animal_chosen.grid(row=1, column=0)

animal_name=tk.Label(animal_selection_frame, text="Animal's Name")
animal_name.grid(row=0,column=2)

animal_name_entry=tk.Entry(animal_selection_frame)
animal_name_entry.grid(row=1, column=2)

for widget in animal_selection_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# goes back to home screen
home_button=tb.Button(signup, text="Home",bootstyle = 'light',command=lambda: homescreen.tkraise(),cursor='hand2')
home_button.grid(row=2, column=0, sticky='sw',padx=5,pady=5)

# if all required fields are satisfied, will navigate to save files
create_account_button=tb.Button(signup,text="Create Account",bootstyle = 'success', command=lambda: savefile.tkraise(),cursor='hand2')
create_account_button.grid(row=2, column=0, sticky='se',padx=5,pady=5)

savefile.rowconfigure(0, weight=1)
savefile.columnconfigure(0, weight=1)

continue_file_frame=tk.LabelFrame(savefile,text="Save File 1")
continue_file_frame.grid(row=0, column=0, padx=20,pady=20,sticky='nsew')

# continues save data; goes to play screen with pet
continue_button=tb.Button(continue_file_frame, text="Continue", bootstyle='success', command=lambda: mainscreen.tkraise(), cursor='hand2')
continue_button.grid(row=0, column=0,sticky='ew')

# deletes save data and makes it a "new file"
delete_save_button=tb.Button(continue_file_frame,text="Delete Save", bootstyle='danger', cursor='hand2')
delete_save_button.grid(row=1,column=0,sticky='ew')

# doesnt display anything because empty save file
animal_name2=tk.Label(continue_file_frame,text="Animal Name")
animal_name2.grid(row=0,column=1)

# doesnt display anything because empty save file
time_spent_label=tk.Label(continue_file_frame,text="Time Spent")
time_spent_label.grid(row=1,column=1)

for widget in continue_file_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

# label frame for new save file
new_save_frame=tk.LabelFrame(savefile,text="New Save File")
new_save_frame.grid(row=1,column=0,padx=20,pady=20,sticky='nsew')

new_game_button=tb.Button(new_save_frame,text="New File", bootstyle='secondary',command=lambda: mainscreen.tkraise(), cursor="hand2")
new_game_button.grid(row=0,column=0,sticky='ew')

# will update to show animals name
animal_placeholder=tk.Label(new_save_frame,text="_____")
animal_placeholder.grid(row=0,column=1)

# will update to show total time spent since "adoption"
time_placeholder=tk.Label(new_save_frame,text="______")
time_placeholder.grid(row=1,column=1)

for widget in new_save_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

home_button2=tb.Button(savefile, text="Home",bootstyle = 'light',command=lambda: homescreen.tkraise(),cursor='hand2')
home_button2.grid(row=2, column=0, sticky='sw',padx=5,pady=5)

mainscreen.rowconfigure(0)  
mainscreen.rowconfigure(1)  
mainscreen.rowconfigure(2)
mainscreen.columnconfigure(0)
mainscreen.columnconfigure(1)
mainscreen.columnconfigure(2)

# label frame containing play/feed/sleep buttons
activity_buttons_frame=tk.LabelFrame(mainscreen, text="Activity")
activity_buttons_frame.grid(row=1,column=1,padx=20,pady=(20,10),sticky='n')

# all 3 buttons need additional frame
play_button=tb.Button(activity_buttons_frame,text="Play",bootstyle='info',cursor='hand2')
play_button.grid(row=0,column=0,sticky='ew')

feed_button=tb.Button(activity_buttons_frame,text="Feed",bootstyle='warning',cursor='hand2')
feed_button.grid(row=0,column=1,sticky='ew')

sleep_button=tb.Button(activity_buttons_frame,text="Sleep",bootstyle='primary',cursor='hand2')
sleep_button.grid(row=0,column=2,sticky='ew')

for widget in activity_buttons_frame.winfo_children():
    widget.grid_configure(padx=5,pady=10)

home_button3=tb.Button(mainscreen, text="Home",bootstyle = 'light',command=lambda: homescreen.tkraise(),cursor='hand2')
home_button3.grid(row=2, column=0, sticky='sw',padx=20,pady=20)

homescreen.tkraise()
root.title("Tomogatchi")
root.resizable(False, False)
root.mainloop()