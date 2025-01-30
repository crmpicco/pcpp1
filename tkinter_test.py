import sys
import tkinter as tk
import os
from tkinter import PhotoImage
from football_api_lookup import get_rangers_players

# grab the API key from the environment variables
football_api_key = os.environ.get("FOOTBALL_API_KEY")
if not football_api_key:
    print("FOOTBALL_API_KEY environment variable not set")
    sys.exit(1)

# Get the Rangers players
rangers_players = get_rangers_players(football_api_key)
if rangers_players and "response" in rangers_players:
    print(rangers_players["response"])
    # for player in rangers_players["response"]:
    #     print(player["player"]["name"])  # Print player name
else:
    print("Error fetching player data.")

# Create the main window
root_window = tk.Tk()
root_window.title("Rangers FC fixtures")

# configure the background image
background_image = PhotoImage(file="rangers-bg.png")
background_label = tk.Label(root_window, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window

# Get the screen dimensions
screen_width = root_window.winfo_screenwidth()
screen_height = root_window.winfo_screenheight()

window_width = 800
window_height = 800

# calculate the position for centering the window vertically and horizontally
center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# position the window in the center of the screen
root_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# disable both horizontal and vertical resizing
root_window.resizable(False, False)

switch = tk.IntVar()
switch.set(0)

check_button = tk.Checkbutton(root_window, text="Check button", variable=switch)
check_button.pack()

# Create a close button which will destroy the window entirely
close_button = tk.Button(
    root_window,
    text="Close",
    command=root_window.destroy,
    bg=root_window.cget("background"),
    bd=0,
    highlightthickness=0,
    activebackground=root_window.cget("background")
)
close_button.pack(side="bottom", pady=20)

# Run the Tkinter event loop
root_window.mainloop()