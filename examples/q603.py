import tkinter as tk

def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    print(f"Selected item: {selected_item}")

root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack()

# Add items to the Listbox
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)

# Bind the on_select function to the Listbox selection event
listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
