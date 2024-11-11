import tkinter as tk
from tkinter import ttk
#import customtkinter as ctk
from PIL import Image, ImageTk
import tomogatchiGUI

def update_hunger_bar(hunger_bar, countdown_time):
    if countdown_time > 100:
        countdown_time = 100

    if countdown_time > 0:
        countdown_time -= 1
        hunger_bar["value"] = countdown_time
        hunger_bar.after(1000, lambda: update_hunger_bar(hunger_bar, countdown_time))
    else:
        hunger_bar["value"] = 0

def update_happiness_bar(happiness_bar, countdown_time):
    if countdown_time > 0:
        countdown_time -= 1
        happiness_bar["value"] = countdown_time
        happiness_bar.after(1000, lambda: update_happiness_bar(happiness_bar, countdown_time))
    else:
        happiness_bar["value"] = 0

def update_energy_bar(energy_bar, countdown_time):
    if countdown_time > 0:
        countdown_time -= 1
        energy_bar["value"] = countdown_time
        energy_bar.after(1000, lambda: update_energy_bar(energy_bar, countdown_time))
    else:
        energy_bar["value"] = 0

def add_to_bar(health_bar, increase=5):
    # max value is 100
    new_value = min(health_bar["valu"] + increase, 100)
    health_bar["value"] = new_value
    # Bar style indicates which bar to update
    if health_bar["style"] == "info.Striped.TProgressbar":
        update_happiness_bar(health_bar, new_value)
    elif health_bar["style"] == "warning.Striped.TProgressbar":
        update_hunger_bar(health_bar, new_value)
    elif health_bar["style"] == "primary.Striped.TProgressbar":
        update_energy_bar(health_bar, new_value)
