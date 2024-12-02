import application
import random
from Sprite_Stuff import SpriteSheetFramework as sprite
import time
from PIL import Image, ImageTk

def trigger_animation_update(self, state):
        self.petState = state
        self.is_busy = True
        if state == 1: 
            application.add_to_bar(self.happiness_bar, application.update_happiness_bar)
        elif state == 2:
            application.add_to_bar(self.hunger_bar, application.update_hunger_bar)
        elif state == 3:
            application.add_to_bar(self.energy_bar, application.update_energy_bar)

def sprite_animation(self):
    # Run this in a loop to handle animation
    while not self.stop_animation:
        if self.is_busy:
            play_activity_animation(self)
            self.is_busy = False
            self.petState = 0  # Return to idle state
        else:
            play_idle_animation(self)

def randomIdle(self):
    i = random.randint(4, 6)
    for frame_index in range(len(self.pet.frame[i])):
        if self.is_busy:
            break
        update_sprite(self, i, frame_index)
        time.sleep(0.2)

def play_idle_animation(self):
    for frame_index in range(len(self.pet.frame[0])):  # Loop through idle frames
        if self.is_busy:
            break  # Interrupt idle if an activity is triggered
        update_sprite(self, 0, frame_index)
        time.sleep(0.3)  # Control frame rate
    # 12% chance for a random idle animation after a full loop
    if random.randint(0, 100) <= 12:
        randomIdle(self) 

def play_activity_animation(self):
    i = self.petState
    for frame_index in range(len(self.pet.frame[self.petState])):  # Loop through activity frames
        # Prevents the animation from crashing upon changing the activity 
        if i != self.petState:
            play_activity_animation(self)
            break
        update_sprite(self, self.petState, frame_index)
        time.sleep(0.2)  # Control frame rate
    
    #Keeps the sprite playing (durring sleep or death)
    while self.petState == 7:
        play_activity_animation(self)

def update_sprite(self, y, frame_index):
    # Retrieve and update the image for the current frame
    frame_image = self.pet.FrameGet(y, frame_index)
    self.current_img = ImageTk.PhotoImage(frame_image)
    self.image_label.config(image=self.current_img)

def stop_animation(self):
    self.stop_animation = True
