import tkinter as tk

def remove_frame():
    frame.detach()

root = tk.Tk()
root.title("Frame Example")

frame = tk.Frame(root, width=200, height=100, bg="red")
frame.pack()

remove_button = tk.Button(root, text="Remove Frame", command=remove_frame)
remove_button.pack()

root.mainloop()
