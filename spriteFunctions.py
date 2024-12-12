import application
import random
from Sprite_Stuff import SpriteSheetFramework as sprite
import time
from PIL import ImageTk

revived = False
stopThread = False

def trigger_animation_update(self, state):
    self.petState = state
    self.is_busy = True

    if state == 1:  # Happiness
        application.add_to_bar(self.happiness_bar, 3000)
    elif state == 2:  # Hunger
        application.add_to_bar(self.hunger_bar, 3000)
    elif state == 3:  # Energy
        application.add_to_bar(self.energy_bar, 12000)

def home_animation(self, state):
    self.petState = state
    self.is_busy = True

def sprite_animation(self):
    global revived, stopThread
    # Run this in a loop to handle animation
    while not self.stop_animation:
        if stopThread == True:
            #This is for when the user goes back home
            print("ThreadStopped")
            break
        #faint check
        faint = application.faintCheck()
        if faint == True:
            play_activity_animation(self)

        if self.is_busy:
            play_activity_animation(self)
            self.is_busy = False
            if revived == False:
                self.petState = 0  # Return to idle state
            else:
                # Waves when revived
                revived = False
                self.petState = 1
                play_activity_animation(self)
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
    # If the pet is fainted, this will force it into the "fainted" state
    global revived
    faint = application.faintCheck()
    if faint == False:
        i = self.petState
    else:
        revived = True
        self.petState = 7
        i = 7

    for frame_index in range(len(self.pet.frame[self.petState])):  # Loop through activity frames
        # Prevents the animation from crashing upon changing the activity 
        if i != self.petState:
            play_activity_animation(self)
            break
        update_sprite(self, self.petState, frame_index)
        time.sleep(0.2)  # Control frame rate
    
    #Keeps the sprite playing For when it faints
    while self.petState == 7:
        play_activity_animation(self)

def update_sprite(self, y, frame_index):
    # Retrieve and update the image for the current frame
    frame_image = self.pet.FrameGet(y, frame_index)
    self.current_img = ImageTk.PhotoImage(frame_image)
    self.image_label.config(image=self.current_img)

def stop_animation(self):
    self.stop_animation = True

def stop_Thread():
    global stopThread
    stopThread = True

def start_Thread():
    global stopThread
    stopThread = False