import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize the root window
root = tk.Tk()
root.title("Countdown with Image Background")
root.geometry("800x600")  # Set the window size

# Load and set the background image
background_image = Image.open(r"C:\Users\karti\Downloads\python\image1.jpg")
background_image = background_image.resize((1900, 1550), Image.LANCZOS)  # Resize to fit window
bg_image = ImageTk.PhotoImage(background_image)

# Create a canvas to place the background image and text
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

# Place the image in the background
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Add the main text label on top of the background
main_text = canvas.create_text(
    400, 250,
    text="Two Months Until the Start\nof a Beautiful Journey",
    font=("Helvetica", 48, "bold"),
    fill="black"
)

# Add the "#Shivit forever" text separately in blue
hashtag_text = canvas.create_text(
    400, 400,
    text="#Shivit forever",
    font=("Helvetica", 48, "bold"),
    fill="orange"
)

# Function to make the text blink
def blink_text():
    current_color = canvas.itemcget(main_text, "fill")
    next_color = "blue" if current_color == "blue" else "black"
    canvas.itemconfig(main_text, fill=next_color)
    root.after(500, blink_text)  # Blink every 500ms

# Function to change the background color slightly (overlay)
def change_background_tint():
    colors = ["#FFB3B3", "#B3FFC2", "#B3D9FF", "#FFB3D9", "#FFF4B3"]
    canvas.config(bg=random.choice(colors))
    root.after(1000, change_background_tint)  # Change tint every 1000ms

# Start the blinking text and background color change
blink_text()
change_background_tint()

# Run the Tkinter event loop
root.mainloop()
