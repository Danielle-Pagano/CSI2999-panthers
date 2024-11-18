import app
from Sprite_Stuff import SpriteSheetFramework as sprite
import time
from PIL import Image, ImageTk

def trigger_animation_update(self, state):
        self.petState = state
        self.is_busy = True
        if state == 1: 
            app.add_to_bar(self.happiness_bar, app.update_happiness_bar)
        elif state == 2:
            app.add_to_bar(self.hunger_bar, app.update_hunger_bar)
        elif state == 3:
            app.add_to_bar(self.energy_bar, app.update_energy_bar)

def sprite_animation(self):
    # Run this in a loop to handle animation
    while not self.stop_animation:
        if self.is_busy:
            play_activity_animation(self)
            self.is_busy = False
            self.petState = 0  # Return to idle state
        else:
            play_idle_animation(self)

def play_idle_animation(self):
    for frame_index in range(len(self.pet.frame[0])):  # Loop through idle frames
        if self.is_busy:
            break  # Interrupt idle if an activity is triggered
        update_sprite(self, 0, frame_index)
        time.sleep(0.3)  # Control frame rate

def play_activity_animation(self):
    for frame_index in range(len(self.pet.frame[self.petState])):  # Loop through activity frames
        update_sprite(self, self.petState, frame_index)
        time.sleep(0.3)  # Control frame rate

def update_sprite(self, y, frame_index):
    # Retrieve and update the image for the current frame
    frame_image = self.pet.FrameGet(y, frame_index)
    self.current_img = ImageTk.PhotoImage(frame_image)
    self.image_label.config(image=self.current_img)

def stop_animation(self):
    self.stop_animation = True
