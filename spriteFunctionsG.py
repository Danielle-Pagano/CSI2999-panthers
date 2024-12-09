import application
import random
from Sprite_Stuff import SpriteSheetFramework as sprite
from PIL import ImageTk

def trigger_animation_update(self, state):
    self.petState = state
    self.is_busy = True
    if state == 1:  # Happiness
        if hasattr(self, 'happiness_bar'):
            application.add_to_bar(self.happiness_bar, 10)
        else:
            print("Happiness bar is not initialized.")

    elif state == 2:  # Hunger
        if hasattr(self, 'hunger_bar'):
            application.add_to_bar(self.hunger_bar, 15)
        else:
            print("Hunger bar is not initialized.")

    elif state == 3:  # Energy
        if hasattr(self, 'energy_bar'):
            application.add_to_bar(self.energy_bar, 20)
        else:
            print("Energy bar is not initialized.")

def sprite_animation(self):
    if not hasattr(self, 'animation_initialized'):
        self.animation_initialized = True
        self.after(1000, lambda: sprite_animation(self))  # Wait for UI rendering
        return
    if self.is_busy:
        play_activity_animation(self)
        self.is_busy = False
        self.petState = 0
    else:
        play_idle_animation(self)
    self.after(1000, lambda: sprite_animation(self))

def play_idle_animation(self):
    def update_frame(index):
        if not self.is_busy:
            update_sprite(self, 0, index)
            if index + 1 < len(self.pet.frame[0]):
                self.after(150, lambda: update_frame(index + 1))
            elif random.randint(0, 100) <= 12:  # Random idle chance
                random_idle(self)
    update_frame(0)

def play_activity_animation(self):
    def update_frame(index):
        if self.petState == 0 or self.is_busy:
            return
        update_sprite(self, self.petState, index)
        if index + 1 < len(self.pet.frame[self.petState]):
            self.after(1000, lambda: update_frame(index + 1))
    update_frame(0)

def random_idle(self):
    def update_frame(index):
        if not self.is_busy:
            update_sprite(self, 4, index)
            if index + 1 < len(self.pet.frame[4]):
                self.after(1000, lambda: update_frame(index + 1))
    update_frame(0)

def update_sprite(self, y, frame_index):
    frame_image = self.pet.FrameGet(y, frame_index)
    self.current_img = ImageTk.PhotoImage(frame_image)
    self.image_label.config(image=self.current_img)
