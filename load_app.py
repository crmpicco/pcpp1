import sys
import tkinter as tk
import os
from tkinter import PhotoImage, messagebox
from football_api_lookup import FootballApi

# grab the API key from the environment variables
football_api_key = os.environ.get("FOOTBALL_API_KEY")
if not football_api_key:
    print("FOOTBALL_API_KEY environment variable not set")
    sys.exit(1)

# Get the Rangers players
football_api_lookup = FootballApi(football_api_key)
rangers_fixtures = football_api_lookup.get_fixtures(257, 2021)
if not rangers_fixtures and "response" not in rangers_fixtures:
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

search_frame = tk.Frame(root_window)
search_frame.place(relx=0.5, rely=0.5, anchor="center")

# grid layout
team_entry = tk.Entry(search_frame, fg="grey")
team_entry.insert(0, "Enter team name")  # some placeholder text
team_entry.bind("<FocusIn>", team_entry_widget_focus_in)
team_entry.bind("<FocusOut>", team_entry_widget_focus_out)
team_entry.grid(row=0, column=0, padx=10, pady=10)

def search_fixtures():
    team_name = team_entry.get().strip()
    if team_name == "" or team_name == "Enter team name":
        messagebox.showwarning("Input Error", "Please enter a team name to search.")
        return

    search_results = FootballApi.search_fixtures(team_name, rangers_fixtures.get("response", []))
    print(search_results)

    if not isinstance(search_results, list) or not search_results:
        messagebox.showinfo("No Results", f"No matching fixtures found for {team_name}")
    else:
        # create table headers
        headers = search_results[0]  # the first row is the header
        for col_num, header in enumerate(headers):
            header_label = tk.Label(frame_table, text=header, font=('Arial', 10, 'bold'), width=20, anchor="w", relief="solid")
            header_label.grid(row=0, column=col_num)

        # Display search results in table
        # Iterate over search results and populate the table
        for row_num, fixture in enumerate(search_results, start=1):
            tk.Label(frame_table, text=fixture['home_team']).grid(row=row_num, column=0)
            tk.Label(frame_table, text=fixture['away_team']).grid(row=row_num, column=1)
            tk.Label(frame_table, text=fixture['fixture_date']).grid(row=row_num, column=2)
            tk.Label(frame_table, text=fixture['home_score']).grid(row=row_num, column=3)
            tk.Label(frame_table, text=fixture['away_score']).grid(row=row_num, column=4)

# Search button
search_button = tk.Button(search_frame, text="Search for result", command=search_fixtures)
search_button.grid(row=0, column=1, padx=10, pady=10)

switch = tk.IntVar()
switch.set(0)

# Frame to hold the table
frame_table = tk.Frame(root_window)
frame_table.grid(row=2, column=0, padx=10, pady=10)

check_button = tk.Checkbutton(search_frame, text="Check button", variable=switch)
check_button.grid(row=1, column=0, padx=10, pady=10)

# Create a close button which will destroy the window entirely
close_button = tk.Button(
    search_frame,
    text="Close",
    command=root_window.destroy,
    bg=root_window.cget("background"),
    bd=0,
    highlightthickness=0,
    activebackground=root_window.cget("background")
)
close_button.grid(row=1, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root_window.mainloop()
