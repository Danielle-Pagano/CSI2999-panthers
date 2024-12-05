import tkinter as tk
from tkinter import ttk

available_animals = ["Squirrel", "Pigeon"]

def valid_firstname(first_name_entry):
        first_name = first_name_entry.get().strip()
        return bool(first_name)

def valid_lastname(last_name_entry):
        last_name = last_name_entry.get().strip()
        return bool(last_name)

def valid_password(password_entry):
      password = password_entry.get().strip()
      return bool(password)

def valid_email(email_entry):
        email = email_entry.get().strip()
        return "@" in email and "." in email

def valid_age(age_entry):
    try:
        age = int(age_entry.get().strip())
        return age > 0 and age < 100
    except ValueError:
         return False

def valid_animal(animal_entry):
        animal = animal_entry.get().strip().lower()
        return animal in [a.lower() for a in available_animals]

def valid_animal_name(animal_name_entry):
      animal_name = animal_name_entry.get().strip()
      return bool(animal_name)
    
def valid_requirements(firstname_entry, lastname_entry, password_entry, email_entry, animal_entry, animal_name_entry, age_entry):
    return (valid_firstname(firstname_entry) and valid_lastname(lastname_entry) and valid_password(password_entry) and valid_email(email_entry)
            and valid_animal(animal_entry) and valid_animal_name(animal_name_entry) and valid_age(age_entry))

def requirements_met(parent, controller, x_place, y_place, firstname_entry, lastname_entry, password_entry, email_entry, animal_entry, animal_name_entry, age_entry):
    
      for widget in parent.place_slaves():
        if isinstance(widget, tk.Label):
            widget.place_forget()
    
      if (not firstname_entry.get().strip() or not lastname_entry.get().strip() or not email_entry.get().strip() or not password_entry.get().strip()
        or not animal_entry.get().strip() or not animal_name_entry.get().strip() or not age_entry.get().strip()):
          
          error_message = ttk.Label(parent, text="Please fill all required fields", foreground='red')
          error_message.place(x=x_place, y=y_place)
          return False

      if not valid_requirements(firstname_entry, lastname_entry, password_entry, email_entry, animal_entry, animal_name_entry, age_entry):
          error_message = ttk.Label(parent, text="One or more fields are invalid",foreground='red')
          error_message.place(x=x_place, y=y_place)
          return False
    
      for widget in parent.place_slaves():
            if isinstance(widget, tk.Label):
                  info = widget.place_info()
                  if info['x'] == str(x_place) and info['y'] == str(y_place):
                        widget.place_forget()

      controller.show_frame("SaveFileScreen")
      return True