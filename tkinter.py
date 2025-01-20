import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter Window")

# Create a button
button = tk.Button(root, text="Click Me again", command=lambda: print("Button clicked!"))
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()