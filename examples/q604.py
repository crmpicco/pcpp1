import tkinter as tk

root = tk.Tk()
root.title("Widgets at (0, 0)")

button1 = tk.Button(root, text="Button 1 at (0, 0)")
button1.grid(row=0, column=0)

root.mainloop()
