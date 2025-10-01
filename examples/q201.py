import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("My First Tkinter App")

# Add widgets (buttons, labels, etc.) and other elements to the window
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me!")
button.pack()

# Start the event loop (main loop) to display the window
root.mainloop()
