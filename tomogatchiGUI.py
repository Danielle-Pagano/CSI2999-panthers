import tkinter as tk
from tkinter import *
from tkinter import font

root = tk.Tk()

style1 = font.Font(size=25)
style2 = font.Font(size = 20)

homescreen = Frame(root)
signup = Frame(root)
savefile = Frame(root)
mainscreen = Frame(root)

homescreen.grid(row=0, column=0, sticky="nsew")
signup.grid(row=0, column=0, sticky="nsew")
savefile.grid(row=0, column=0, sticky="nsew")
mainscreen.grid(row=0, column=0, sticky="nsew")

lb0 = Label(homescreen, text="Tomogatchi", font=style1)
lb0.pack(pady=20)

lb1 = Label(signup, text="Sign Up", font=style1)
lb1.pack(pady=20)

lb2 = Label(savefile, text="Select Save File", font=style1)
lb2.pack(pady=30)

lb3 = Label(mainscreen, text="Pet Name", font=style1)
lb3.pack(pady=30)

def remove_placeholder(event=None):
    if username.get() == "":
        username_placeholder.place(x=50, y=100)
    else:
        username_placeholder.place_forget()


username = tk.Entry(homescreen, font=('Bold', 15))
username.pack(pady=20)
username.bind('<FocusIn>', remove_placeholder)
username.bind('<FocusOut>', remove_placeholder)

username_placeholder = tk.Label(homescreen, text='User Name', fg='gray', font=('Bold', 12), bg='white')
username_placeholder.place(x=50, y=100)
username_placeholder.bind('<Button-1>', lambda e: username.focus())


password = tk.Entry(homescreen, font=('Bold', 15))
password.pack(pady=20)
password.bind('<FocusIn>', remove_placeholder)
password.bind('<FocusOut>', remove_placeholder)

password_placeholder = tk.Label(homescreen, text='Password', fg='gray', font=('Bold', 12), bg='white')
password_placeholder.place(x=50, y=150)
password_placeholder.bind('<Button-1>', lambda e: password.focus())

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

root.geometry("700x700")
root.title("Tomogatchi")
root.resizable(False, False)
root.mainloop()