import tkinter as tk
import random

# Create the root window
root = tk.Tk()
root.title("Countdown")
root.geometry("600x400")

# Set up the label with the text
label = tk.Label(root, text="Two months to go \n #SHIVIT", font=("Helvetica", 48, "bold"))
label.pack(expand=True)

# Function to make the text blink
def blink_text():
    current_color = label.cget("foreground")
    next_color = "black" if current_color == "red" else "red"
    label.config(foreground=next_color)
    root.after(500, blink_text)  # Blink every 500ms

# Function to change background color randomly
def change_background():
    colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#F3FF33"]
    root.config(bg=random.choice(colors))
    root.after(1000, change_background)  # Change background every 1000ms

# Start the blinking and background color change
blink_text()
change_background()

# Run the Tkinter event loop
root.mainloop()
