import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


class petViewPage:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(window, bg="#000000")

        # Labels for user information
        self.user_info_label = tk.Label(self.frame, text="", bg="#333333", fg="white", font=("Arial", 15))
        self.user_info_label.pack()

        # Firebase Storage URLs for GIFs
        self.gif_urls = {
            "squirrel": "https://firebasestorage.googleapis.com/v0/b/petstkinter.firebasestorage.app/o/gifs%2Fsquirrel%2Fidle_Squirrel.gif?alt=media&token=41d6fdc1-cfb2-48e6-bf84-464db0332e6c",
            "pigeon": "https://firebasestorage.googleapis.com/v0/b/petstkinter.firebasestorage.app/o/gifs%2Fpigeon%2Fidle_pigeon.gif?alt=media&token=e8bc6722-06f7-4d43-9252-206106d57e11",
        }

    def update_user_info(self, first_name, last_name, pet_name):
        # Update the user info label
        self.user_info_label.config(text=f"Name: {first_name} {last_name}\nPet: {pet_name}")

    def load_and_display_gif(self, url):
        # Fetch the GIF data from the URL
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        gif_data = BytesIO(response.content)

        # Load GIF frames
        gif_image = Image.open(gif_data)
        self.frames = []
        try:
            while True:
                frame = ImageTk.PhotoImage(gif_image.copy())
                self.frames.append(frame)
                gif_image.seek(len(self.frames))  # Move to the next frame
        except EOFError:
            pass  # End of GIF frames

        # Display the animation
        self.current_frame = 0
        self.idle_gif_label = tk.Label(self.frame, bg="#000000")
        self.idle_gif_label.pack()
        self.animate_gif()

    def animate_gif(self):
        # Update the displayed frame
        if self.frames:
            frame = self.frames[self.current_frame]
            self.idle_gif_label.config(image=frame)
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame.after(200, self.animate_gif)  # Adjust speed as needed

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
