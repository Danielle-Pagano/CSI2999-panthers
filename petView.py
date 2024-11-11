import tkinter as tk
from PIL import Image, ImageTk

class petViewPage:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(window, bg="#000000")

        # Load the GIF frames
        idle_squirrel = "/Users/ggvhs/Desktop/Projects/pets/pets/images/idle_Squirrel.gif"
        info = Image.open(idle_squirrel)

        # Retrieve the number of frames
        frames = info.n_frames
        photoimage_objects = []
        for i in range(frames):
            obj = tk.PhotoImage(file=idle_squirrel, format=f"gif -index {i}")
            photoimage_objects.append(obj)
    
        # Define the animation function
        def idleAnimation(current_frame=0):
            image = photoimage_objects[current_frame]
            self.idle_gif_label.configure(image=image)
            current_frame = (current_frame + 1) % frames  # Loop back to the first frame
            self.frame.after(200, idleAnimation, current_frame)  # Run the function again after 200ms

        # Create the label widget for displaying the GIF animation
        self.idle_gif_label = tk.Label(self.frame, image=photoimage_objects[0], bg="#000000")
        self.idle_gif_label.pack()

        # Start the animation
        idleAnimation()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
