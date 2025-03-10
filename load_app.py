import sys
import tkinter as tk
import os
from tkinter import PhotoImage, messagebox
from football_api_lookup import FootballApi
from datetime import datetime
import webbrowser

# grab the API key from the environment variables
football_api_key = os.environ.get("FOOTBALL_API_KEY")
if not football_api_key:
    print("FOOTBALL_API_KEY environment variable not set")
    sys.exit(1)

TEAM_ID = 257  # Rangers FC team ID
SEASON = 2021  # 2021 season, only the 2021 season is supported on the Football API free tier

football_api_lookup = FootballApi(football_api_key)
rangers_fixtures = football_api_lookup.get_fixtures(TEAM_ID, SEASON)
if not rangers_fixtures and "response" not in rangers_fixtures:
    print("Error fetching fixtures")

# create the main window for the app
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

# top right and top left circles
canvas = tk.Canvas(root_window, width=100, height=100, bg=root_window.cget("background"), highlightthickness=0)
canvas.place(relx=0.98, y=10, anchor="ne")
canvas.create_oval(0, 0, 100, 100, fill="#1b458f")
canvas.create_text(50, 50, text="Rangers FC\n2021", font=("Arial", 12), anchor="center", justify="center")

canvas = tk.Canvas(root_window, width=100, height=100, bg=root_window.cget("background"), highlightthickness=0)
canvas.place(relx=0.02, y=10, anchor="nw")
canvas.create_oval(0, 0, 100, 100, fill="#1b458f")
canvas.create_text(50, 50, text="Rangers FC\n2021", font=("Arial", 12), anchor="center", justify="center")

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

# automatically set focus on the team entry widget after 5 seconds
root_window.after(5000, lambda: team_entry.focus_set())

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

    # clear previous results in the table
    for widget in frame_table.winfo_children():
        widget.destroy()

    if not isinstance(search_results, list) or not search_results:
        messagebox.showinfo(
            title="No Results",
            message=f"There were no matching fixtures found for Rangers vs {team_name}"
        )
        return

    # make the table visible again after performing the search
    frame_table.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # configure grid columns to have equal width (33% each)
    frame_table.columnconfigure(0, weight=1, minsize=100)
    frame_table.columnconfigure(1, weight=1, minsize=100)
    frame_table.columnconfigure(2, weight=1, minsize=100)

    # create table headers
    header_label = tk.Label(frame_table, text="Home Team", font=('Arial', 10, 'bold'), anchor="w", relief="solid")
    header_label.grid(row=0, column=0)
    header_label = tk.Label(frame_table, text="Away Team", font=('Arial', 10, 'bold'), anchor="w", relief="solid")
    header_label.grid(row=0, column=1)
    header_label = tk.Label(frame_table, text="Date", font=('Arial', 10, 'bold'), anchor="w", relief="solid")
    header_label.grid(row=0, column=2)

    # display search results in table by iterating over the search results and populate the table
    for row_num, fixture in enumerate(search_results, start=1):

        fixture_date = fixture['fixture_date']
        fixture_date = datetime.fromisoformat(fixture_date)
        fixture_date = datetime.strftime(fixture_date, "%d %B %Y @ %I:%M %p")

        home_team = fixture['home_team']
        away_team = fixture['away_team']
        home_score = fixture['home_score']
        away_score = fixture['away_score']

        # check if we need to filter for Rangers wins
        if filter_rangers_wins.get() == 1:
            # Skip the fixture if Rangers didn't win (either as home or away)
            if not ((home_team == "Rangers" and home_score > away_score)
                or (away_team == "Rangers" and away_score > home_score)):
                continue  # Skip to the next fixture if Rangers didn't win

        tk.Label(frame_table, text=f"{fixture['home_team']} ({fixture['home_score']})").grid(row=row_num, column=0)
        tk.Label(frame_table, text=f"{fixture['away_team']} ({fixture['away_score']})").grid(row=row_num, column=1)
        tk.Label(frame_table, text=fixture_date).grid(row=row_num, column=2)


# variable to store whether the user wants to filter for Rangers wins
filter_rangers_wins = tk.IntVar()
filter_rangers_wins.set(0)

# the Search button to trigger the search of fixtures (needs to be a lambda because command does not support arguments)
search_button = tk.Button(search_frame, text="Search for result", command=lambda: search_fixtures(filter_rangers_wins))
search_button.grid(row=0, column=1, padx=10, pady=10)

# a checkbox to filter for Rangers wins only
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
    activebackground=root_window.cget("background"),
    activeforeground="dark blue"
)
close_button.grid(row=1, column=1, padx=10, pady=10)


def open_easter_egg(event):
    webbrowser.open("https://youtu.be/XitegYosG8s")
    root_window.unbind("<slash>")  # unbind the event on the forward slash so it doesn't trigger again


# hit the forward slash key for an Easter egg ;)
root_window.bind("<slash>", open_easter_egg)

# Run the Tkinter event loop
root_window.mainloop()
