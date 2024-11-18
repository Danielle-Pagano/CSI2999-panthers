import tkinter as tk


available_animals = ["Squirrel"]

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

def requirements_met(parent, controller, firstname_entry, lastname_entry, password_entry, email_entry, animal_entry, animal_name_entry, age_entry):
    if (not firstname_entry.get().strip() or not lastname_entry.get().strip() or not email_entry.get().strip() or not password_entry.get().strip()
        or not animal_entry.get().strip() or not animal_name_entry.get().strip() or not age_entry.get().strip()):
          
          error_message = tk.Label(parent, text="Please fill all required fields", bg="#fff",fg='red')
          error_message.grid(row=2, column=0, sticky='n', pady=(5,0))
          return False
    
    if not valid_requirements(firstname_entry, lastname_entry, password_entry, email_entry, animal_entry, animal_name_entry, age_entry):
          error_message = tk.Label(parent, text="One or more fields are invalid", bg='#fff', fg='red')
          error_message.grid(row=2, column=0, sticky = 'n', pady=(5,0))
          return False
    
    for widget in parent.grid_slaves(row=2, column=0):
          if isinstance(widget, tk.Label):
                widget.grid_forget()

    controller.show_frame("SaveFileScreen")
    return True