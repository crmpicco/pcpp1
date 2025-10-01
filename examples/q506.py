import tkinter as tk
def action_one():
    label.config(text="Button 1 clicked!")
root = tk.Tk()
root.title("Multiple Buttons Example")

label = tk.Label(root, text="Press a button", font=("Arial", 16))
label.pack(pady=10)

button1 = tk.Button(root, text="Button 1", command=action_one)
button1.pack(pady=5)

root.mainloop()
