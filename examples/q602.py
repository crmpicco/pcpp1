import tkinter as tk

root = tk.Tk()

# Create two labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")

# Position the labels in the grid
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.mainloop()
