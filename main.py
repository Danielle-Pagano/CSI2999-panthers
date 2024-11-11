import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from login import LoginPage
from petView import petViewPage

class MainApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Pet Management App")

        # Initialize pages
        self.login_page = LoginPage(self.window, self.show_petview)
        self.petview_page = petViewPage(self.window)

        # Start with the login page
        self.login_page.show()

    def show_petview(self):
        self.login_page.hide()
        self.petview_page.show()

if __name__ == "__main__":
    window = tk.Tk()
    app = MainApp(window)
    window.mainloop()























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