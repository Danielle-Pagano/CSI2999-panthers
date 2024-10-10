
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Brenner\Desktop\Tomogatchi\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Main window setup
window = Tk()
window.geometry("750x600")
window.configure(bg="#FFFFFF")

# Create Canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=750,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Title text
canvas.create_text(
    267.0,
    57.75,
    anchor="nw",
    text="Tomogatchi",
    fill="#000000",
    font=("Inter", 35 * -1)
)

# Gray rectangle
canvas.create_rectangle(
    81.0,
    193.5,
    669.2783203125,
    418.447265625,
    fill="#D9D9D9",
    outline=""
)

# Labels for input fields
canvas.create_text(
    113.77734375,
    280.8896484375,
    anchor="nw",
    text="Last Name:",
    fill="#000000",
    font=("Itim Regular", 35 * -1)
)

canvas.create_text(
    106.91015625,
    345.427734375,
    anchor="nw",
    text="Email Address:",
    fill="#000000",
    font=("Itim Regular", 35 * -1)
)

canvas.create_text(
    113.77734375,
    216.1142578125,
    anchor="nw",
    text="First Name:",
    fill="#000000",
    font=("Itim Regular", 35 * -1)
)

# Create input fields (Entry boxes)
first_name_entry = Entry(window)
first_name_entry.place(x=303.0, y=218.0, width=240.0, height=40.0)

last_name_entry = Entry(window)
last_name_entry.place(x=303.0, y=286.0, width=240.0, height=40.0)

email_entry = Entry(window)
email_entry.place(x=340.0, y=347.0, width=240.0, height=40.0)

# Load button image
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))

# Create button
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Button clicked!"),
    relief="flat"
)
button_1.place(x=279.0, y=469.0, width=191.0, height=95.0)

# Add text over the button (optional)
canvas.create_text(
    316.0,
    507.0,
    anchor="nw",
    text="Create Account",
    fill="#000000",
    font=("Inter", 16 * -1)
)

window.resizable(False, False)
window.mainloop()