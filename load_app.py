import sys
import tkinter as tk
import os
from tkinter import PhotoImage
from football_api_lookup import FootballApi

# grab the API key from the environment variables
football_api_key = os.environ.get("FOOTBALL_API_KEY")
if not football_api_key:
    print("FOOTBALL_API_KEY environment variable not set")
    sys.exit(1)

# Get the Rangers players
football_api_lookup = FootballApi(football_api_key)
rangers_fixtures = football_api_lookup.get_fixtures(257, 2021)
if rangers_fixtures and "response" in rangers_fixtures:
    print(rangers_fixtures["response"])
    # for player in rangers_players["response"]:
    #     print(player["player"]["name"])  # Print player name
else:
    print("Error fetching player data.")

# Create the main window
root_window = tk.Tk()
root_window.title("Rangers FC fixtures")

# configure the background image. This needs to go before the widgets
background_image = PhotoImage(file="rangers-bg.png")
background_label = tk.Label(root_window, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window # noqa

header = tk.Label(root_window, text="Search Rangers FC fixtures", font=("Helvetica", 24))
header.place(relx=0.5, rely=0.1, anchor="center")

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

grid_frame = tk.Frame(root_window)
grid_frame.grid(row=0, column=0, padx=10, pady=10)


def team_entry_widget_focus_in(event):
    if team_entry.get() == "Enter team name":
        team_entry.delete(0, tk.END)
        team_entry.config(fg="white")


def team_entry_widget_focus_out(event):
    if team_entry.get() == "":
        team_entry.insert(0, "Enter team name")
        team_entry.config(fg="grey")


# grid layout
team_entry = tk.Entry(root_window, fg="grey")
team_entry.insert(0, "Enter team name")  # some placeholder text
team_entry.bind("<FocusIn>", team_entry_widget_focus_in)
team_entry.bind("<FocusOut>", team_entry_widget_focus_out)
team_entry.grid(row=0, column=1, padx=10, pady=10)

# Search button
search_button = tk.Button(grid_frame, text="Search for result")
search_button.grid(row=1, column=1, padx=10, pady=10)

switch = tk.IntVar()
switch.set(0)

pack_frame = tk.Frame(root_window)
pack_frame.grid(row=3, column=1, padx=10, pady=10)

check_button = tk.Checkbutton(pack_frame, text="Check button", variable=switch)
check_button.pack()

# Create a close button which will destroy the window entirely
close_button = tk.Button(
    pack_frame,
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
