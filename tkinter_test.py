import sys
import tkinter as tk
import os
from tkinter import PhotoImage

# grab the API key from the environment variables
football_api_key = os.environ.get("FOOTBALL_API_KEY")
if not football_api_key:
    print("FOOTBALL_API_KEY environment variable not set")
    sys.exit(1)

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter Window")

# configure the background image
background_image = PhotoImage(file="rangers-bg.png")
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 800
window_height = 800

# calculate the position for centering the window vertically and horizontally
center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# position the window on the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# disable both horizontal and vertical resizing
root.resizable(False, False)

# Create a button
button = tk.Button(root, text="Click Me again", command=lambda: print("Button clicked!"))
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()