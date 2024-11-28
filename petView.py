import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


class petViewPage:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(window, bg="#000000")

        # Firebase Storage URLs for GIFs (replace with actual URLs)
        self.gif_urls = {
            "squirrel": "https://firebasestorage.googleapis.com/v0/b/YOUR_PROJECT_ID/o/gifs%2Fsquirrel.gif?alt=media",
            "pigeon": "https://firebasestorage.googleapis.com/v0/b/YOUR_PROJECT_ID/o/gifs%2Fpigeon.gif?alt=media",
        }

        # Default GIF
        self.load_and_display_gif(self.gif_urls["squirrel"])

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
