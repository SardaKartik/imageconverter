import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize the root window
root = tk.Tk()
root.title("Countdown with Image Background")
root.geometry("800x600")  # Set the window size

# Load and set the background image
background_image = Image.open(r"C:\Users\karti\Downloads\python\image1.jpg")
background_image = background_image.resize((800, 600), Image.LANCZOS)  # Resize to fit window
bg_image = ImageTk.PhotoImage(background_image)

# Create a canvas to place the background image and text
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

# Place the image in the background
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Initial text and maximum font size
text = "Two months to go for the wedding of my sister!"
font_size = 48  # Start with a large font size

# Function to dynamically adjust the font size to fit within canvas width
def fit_text():
    global font_size, label
    while True:
        font = ("Helvetica", font_size, "bold")
        temp_id = canvas.create_text(400, 300, text=text, font=font, fill="red")
        text_width = canvas.bbox(temp_id)[2] - canvas.bbox(temp_id)[0]
        canvas.delete(temp_id)  # Remove temporary text for size testing
        if text_width <= canvas.winfo_width() - 20:  # Leave padding
            break
        font_size -= 2  # Decrease font size until it fits

    # Final text with fitted font size
    label = canvas.create_text(400, 300, text=text, font=("Helvetica", font_size, "bold"), fill="red")

# Function to make the text blink
def blink_text():
    current_color = canvas.itemcget(label, "fill")
    next_color = "black" if current_color == "red" else "red"
    canvas.itemconfig(label, fill=next_color)
    root.after(500, blink_text)  # Blink every 500ms

# Function to change the background color slightly (overlay)
def change_background_tint():
    colors = ["#FFB3B3", "#B3FFC2", "#B3D9FF", "#FFB3D9", "#FFF4B3"]
    canvas.config(bg=random.choice(colors))
    root.after(1000, change_background_tint)  # Change tint every 1000ms

# Start font fitting, blinking text, and background color change
fit_text()
blink_text()
change_background_tint()

# Run the Tkinter event loop
root.mainloop()
