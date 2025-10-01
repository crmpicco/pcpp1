import tkinter as tk

def on_key_press(event):
    key_label.config(text=f"You pressed: {event.char}")

root = tk.Tk()
root.title("Key Press Event")

key_label = tk.Label(root, text="Press a key")
key_label.pack(pady=10)

root.bind("<Key>", on_key_press)
root.mainloop()
