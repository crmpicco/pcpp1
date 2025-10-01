import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(
    root,
    text='Hello, World!',
    fg='white',
    bg='black',
    width=10,
    height=10,
    anchor='center',  
    justify='left'  )
label.pack()

root.mainloop()
