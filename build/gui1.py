


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Brenner\Desktop\Tomogatchi\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("750x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 750,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    55.0,
    106.0,
    684.89306640625,
    457.08795166015625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    315.250244140625,
    225.309814453125,
    509.6241760253906,
    281.7997398376465,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    315.250244140625,
    300.0223388671875,
    509.6241760253906,
    356.512264251709,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    315.250244140625,
    374.73480224609375,
    509.6241760253906,
    431.22472763061523,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    79.57177734375,
    225.309814453125,
    anchor="nw",
    text="New Save File:",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    79.57177734375,
    300.0223388671875,
    anchor="nw",
    text="New Save File:",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    79.57177734375,
    374.73480224609375,
    anchor="nw",
    text="New Save File:",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    79.57177734375,
    150.59735107421875,
    anchor="nw",
    text="Save File 1:",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    292.0,
    30.0,
    anchor="nw",
    text="Tomogatchi",
    fill="#000000",
    font=("Inter", 35 * -1)
)

canvas.create_text(
    357.162109375,
    230.169189453125,
    anchor="nw",
    text="Create",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    357.162109375,
    304.88165283203125,
    anchor="nw",
    text="Create",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    357.162109375,
    374.73480224609375,
    anchor="nw",
    text="Create",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=292.0,
    y=485.0,
    width=191.0,
    height=95.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=315.0,
    y=111.0,
    width=191.0,
    height=95.0
)

canvas.create_text(
    372.0,
    137.0,
    anchor="nw",
    text="Play",
    fill="#000000",
    font=("Itim Regular", 36 * -1)
)

canvas.create_text(
    362.0,
    530.0,
    anchor="nw",
    text="Home",
    fill="#000000",
    font=("Inter", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
