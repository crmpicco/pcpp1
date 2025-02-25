import sys
import tkinter as tk
import os
from tkinter import PhotoImage, messagebox
from football_api_lookup import FootballApi
from datetime import datetime

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

# create the main window
root_window = tk.Tk()
root_window.title("Rangers FC fixtures")
root_window.configure(bg='white')

# configure the background image. This needs to go before the widgets
background_image = PhotoImage(file="rangers-bg.png")
background_label = tk.Label(root_window, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window # noqa

header = tk.Label(
    root_window,
    text="Search Rangers FC Fixtures",
    font=("Impact", 32),
    bg=root_window.cget("background"),
    fg="black",
    highlightthickness=0,
    bd=0
)
header.grid(row=0, column=0, sticky="n", columnspan=2, padx=10, pady=10)

canvas = tk.Canvas(root_window, width=100, height=100, bg=root_window.cget("background"), highlightthickness=0)
canvas.grid(row=1, column=0, pady=10, sticky="n")
canvas.create_oval(0, 0, 100, 100, fill="#1b458f")
canvas.create_text(50, 50, text="Rangers FC\n2021", font=("Arial", 12), anchor="center")

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

# Grid configuration for centering the widgets
root_window.grid_rowconfigure(0, weight=0)  # Row for header, fixed size
root_window.grid_rowconfigure(1, weight=1)  # Row for a search form should expand to fill space
root_window.grid_rowconfigure(2, weight=1)  # Row for the table should expand as well

root_window.grid_columnconfigure(0, weight=1)  # Column for all widgets, should expand horizontally

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
search_frame.grid(row=1, column=0, padx=10, pady=10)

# grid layout
team_entry = tk.Entry(search_frame, fg="grey")
team_entry.insert(0, "Enter team name")
team_entry.bind("<FocusIn>", team_entry_widget_focus_in)
team_entry.bind("<FocusOut>", team_entry_widget_focus_out)
team_entry.grid(row=0, column=0, padx=10, pady=10)

# Frame to hold the table, but hide it initially
frame_table = tk.Frame(root_window)
frame_table.grid_forget()


def search_fixtures(filter_rangers_wins):
    team_name = team_entry.get().strip()
    if team_name == "" or team_name == "Enter team name":
        messagebox.showwarning("Input Error", "Please enter a team name to search.")
        return

    search_results = FootballApi.search_fixtures(team_name, rangers_fixtures.get("response", []))
    print(search_results)

    # Clear previous results in the table
    for widget in frame_table.winfo_children():
        widget.destroy()

    if not isinstance(search_results, list) or not search_results:
        messagebox.showinfo("No Results", f"No matching fixtures found for {team_name}")
    else:
        # Make the table visible again after performing the search
        frame_table.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # create table headers
        headers = search_results[0]  # the first row is the header
        for col_num, header in enumerate(headers):
            header = header.replace("_", " ").title()
            header_label = tk.Label(frame_table, text=header, font=('Arial', 10, 'bold'), width=20, anchor="w", relief="solid")
            header_label.grid(row=0, column=col_num)

        # Display search results in table
        # Iterate over search results and populate the table
        for row_num, fixture in enumerate(search_results, start=1):

            fixture_date = fixture['fixture_date']
            fixture_date = datetime.fromisoformat(fixture_date)
            fixture_date = datetime.strftime(fixture_date, "%d %B %Y @ %I:%M %p")

            home_team = fixture['home_team']
            away_team = fixture['away_team']
            home_score = fixture['home_score']
            away_score = fixture['away_score']

            # Check if we need to filter for Rangers wins
            if filter_rangers_wins.get() == 1:
                # Skip the fixture if Rangers didn't win (either as home or away)
                if not ((home_team == "Rangers" and home_score > away_score) or (away_team == "Rangers" and away_score > home_score)):
                    continue  # Skip to the next fixture if Rangers didn't win

            tk.Label(frame_table, text=fixture['home_team']).grid(row=row_num, column=0)
            tk.Label(frame_table, text=fixture['away_team']).grid(row=row_num, column=1)
            tk.Label(frame_table, text=fixture_date).grid(row=row_num, column=2)
            tk.Label(frame_table, text=fixture['home_score']).grid(row=row_num, column=3)
            tk.Label(frame_table, text=fixture['away_score']).grid(row=row_num, column=4)


filter_rangers_wins = tk.IntVar()
filter_rangers_wins.set(0)

# Search button
search_button = tk.Button(search_frame, text="Search for result", command=lambda: search_fixtures(filter_rangers_wins))
search_button.grid(row=0, column=1, padx=10, pady=10)

rangers_wins_only = tk.Checkbutton(search_frame, text="Rangers wins only", variable=filter_rangers_wins)
rangers_wins_only.grid(row=1, column=0, padx=10, pady=10)

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
