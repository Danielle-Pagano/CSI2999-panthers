import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


window = tk.Tk()
window.title("login form")
#title of the application When being ran

window.geometry('700x700')
#Dimensions of the window upon running app

window.configure(bg="#000000")
#Background color of my window

#Creating a frame to hold the widgets below
login_frame = tk.Frame(window, bg="#000000")
login_frame.pack()

#Creating the logged in page
pet_view_frame = tk.Frame(window, bg="#000000")




#The function for the login
#This is where database intergration starts
def login():
    username = "G"
    password = "G"
    if username_entry.get() == username and password_entry.get() == password:
        print("Successfully logged in")
        login_frame.pack_forget()
        pet_view_frame.pack()
    else:
        print("Invalid Login")


# Creating all the widgets in the login frame
login_label = tk.Label(login_frame, text = "Login", bg="#000000", font=("Arial",30))
username_label = tk.Label(login_frame, text="Username", bg="#000000", font=("Arial",15))
username_entry = tk.Entry(login_frame, highlightthickness=0, bd=0)
password_entry = tk.Entry(login_frame, show="*", highlightthickness=0, bd=0)
password_label = tk.Label(login_frame, text="Password", bg="#000000", font=("Arial",15))
login_button = tk.Button(login_frame,
                         text="Login",
                         highlightthickness=0, 
                         bd=0,
                         bg="#000000", 
                         relief="flat", 
                         highlightbackground="#000000", 
                         highlightcolor="#000000", 
                         font=("Arial",15),
                         command=login )

#Placing login widgets on the login frame
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1, pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)





'''
the section below comprises all of what the user will see once they are loggged in 

and slected their saved pet file.
'''


#Storing the gif into variables/objects
idle_Squirrel = "/Users/ggvhs/Desktop/Projects/pets/pets/images/idle_Squirrel.gif"
info = Image.open(idle_Squirrel)

#retriving number of frames
frames = info.n_frames

#Storing the gif into variables/objects
photoimage_objects = []
for i in range(frames):
    obj = tk.PhotoImage(file=idle_Squirrel, format=f"gif -index {i}")
    photoimage_objects.append(obj)


def idleAnimation(current_frame=0):
    image = photoimage_objects[current_frame]
    idle_gif_label.configure(image=image)
    current_frame = (current_frame + 1) % frames  # Loop back to the first frame
    pet_view_frame.after(200, idleAnimation, current_frame)  # Run the function again after 50ms


# Creating all the widgets in the pet view frame
idle_gif_label = tk.Label(pet_view_frame, image="", bg="#000000")


#Placing all the pet view widgets on the pet view frame
idle_gif_label.pack()
idleAnimation()








window.mainloop()
#^^ This is what the entire program is ran in



























'''
# Global variable for the countdown
countdown_time = 1200  # 20 minutes in seconds

def update_timer():
    global countdown_time
    if countdown_time > 0:
        minutes, seconds = divmod(countdown_time, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        countdown_time -= 1
        # Update timer every 1 second
        window.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")

def startFeedingTimer():
    global countdown_time
    print("Feeding timer has started")
    
    update_timer()  # Start countdown

def resetFeedingTimer():
    global countdown_time
    print("Feeding timer has been reset")
    countdown_time = 1200  # Reset to 20 minutes

# Setup window
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# Import an image
image_original = Image.open('Squirrel.jpg')
image_tk = ImageTk.PhotoImage(image_original)

# Widget 
label = ttk.Label(window, text="squirrel", image=image_tk)
label.pack()

# Timer label
timer_label = ttk.Label(window, text="20:00", font=("Helvetica", 24))
timer_label.pack()

# Wake pet button (starts the timer)
wake_button = ttk.Button(window, text="Wake pet", command=startFeedingTimer)
wake_button.pack()

# Feed me button (resets the timer)
feed_button = ttk.Button(window, text="feed me", command=resetFeedingTimer)
feed_button.pack()

# Run the application
window.mainloop()
'''