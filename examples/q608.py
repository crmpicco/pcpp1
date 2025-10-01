import tkinter as tk
from tkinter import messagebox

def greet_user():
    messagebox.showinfo("Greeting", "Hello, user!")

root = tk.Tk()
root.title("Button Example")

# Create a button with the text "Click Me"
button = tk.Button(root, text="Click Me", command=greet_user)
button.pack(pady=20)

root.mainloop()
