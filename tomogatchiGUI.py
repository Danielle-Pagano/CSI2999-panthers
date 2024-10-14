import tkinter as tk
import tkinter.ttk
from tkinter import *
from tkinter import font

root = tk.Tk()


style1 = font.Font(size=25)
style2 = font.Font(size = 20)

homescreen = tk.Frame(root, height=350)
signup = Frame(root)
savefile = Frame(root)
mainscreen = Frame(root)

homescreen.grid(row=0, column=0, sticky='ew')
signup.grid(row=0, column=0, sticky="nsew")
savefile.grid(row=0, column=0, sticky="nsew")
mainscreen.grid(row=0, column=0, sticky="nsew")

lb0 = Label(homescreen, text="Welcome!", font=style1)
lb0.pack(pady=20)

lb1 = Label(signup, text="Sign Up", font=style1)
lb1.pack(pady=20)

lb2 = Label(savefile, text="Select Save File", font=style1)
lb2.pack(pady=30)

lb3 = Label(mainscreen, text="Pet Name", font=style1)
lb3.pack(pady=30)

def username_click(event):
    if username.get() == "Enter Username":
        username.delete(0, tk.END)
        username.configure(foreground="black")

def username_focus_out(event):
    if username.get() == "":
        username.insert(0, "Enter Username")
        username.configure(foreground="gray")

def password_click(event):
    if password.get() == "Enter Password":
        password.delete(0, tk.END)
        password.configure(foreground="black")

def password_focus_out(event):
    if password.get() == "":
        password.insert(0, "Enter Password")
        password.configure(foreground="gray")



username = tk.Entry(homescreen, font=('Bold', 15))
username.insert(0, "Enter Username")
username.bind('<FocusIn>', username_click)
username.bind('<FocusOut>', username_focus_out)
username.pack()


password = tk.Entry(homescreen, font=('Bold', 15))
password.insert(0, "Enter Password")
password.bind('<FocusIn>', password_click)
password.bind('<FocusOut>', password_focus_out)
password.pack()


signupBut = Button(homescreen, text="Sign Up", command=lambda: signup.tkraise(), font=style2)
signupBut.pack()

loginBut = Button(homescreen, text="Log In", command=lambda: savefile.tkraise(), font=style2)
loginBut.pack()

CAButton = Button(signup, text="Create Account", command=lambda: savefile.tkraise(), font=style2)
CAButton.pack()

newSaveBut = Button(savefile, text="New File", command=lambda: mainscreen.tkraise(), font=style2)
newSaveBut.pack()

continueBut = Button(savefile, text="Continue", command=lambda: mainscreen.tkraise(), font=style2)
continueBut.pack()

playBut = Button(mainscreen, text="Play", font=style2)
playBut.pack()

feedBut = Button(mainscreen, text="Feed", font=style2)
feedBut.pack()

homescreen.tkraise()

root.geometry("700x500")
root.title("Tomogatchi")
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)
root.mainloop()
root.geometry("700x700")
root.title("Tomogatchi")
root.resizable(False, False)
root.mainloop()
