# GUI Programming

## Tkinter

### Events
`<Key>` is a special event that is triggered when any key is pressed. It can be used to bind a function to a key press event.

`<Motion>` is a special event that is triggered when the mouse is moved with a mouse button being held down. It can be used to bind a function to a mouse movement event.

Event handlers interact with various components to capture and transform user input

### Widgets

#### Positioning

The placement of widgets in a window is determined by the geometry manager. They can be defined by x/y coordinates or with relative coordinates and anchor, e.g.
```python
# x/y coordinates (in pixels)
import tkinter as tk
xy_label = tk.Label(root, text="x/y coordinates")
xy_label.place(x=100, y=100)
```
```python
# relative coordinates (and anchor)
import tkinter as tk
relative_label = tk.Label(root, text="relative (anchored) coordinates")
relative_label.place(relx=0.5, rely=0.5, anchor="center")
```

#### Styling
`background` or `bg` - the background colour of the widget

`selectforeground` - the colour of the text when selected

`activebackground` - the background colour of the widget when it is active/under the cursor
 
- `Entry` - a single-line text input field. It can be used to get user input. 
```python
entry.insert(0, "Please enter your name")
entry.insert(5, "*****")
# the Entry widget will display "Pleas*****e enter your name".
```
* `Label` - a widget that displays text or an image. It can be used to display information to the user.
```python
stadium = tk.Label(
    root, 
    text="Stadium",
    fg="white",
    bg="black",
    width=25,  # width and height are measured in text units
    height=25
)
```
* `Frame` - a container widget that can hold other widgets. It can be used to group related widgets together.
You can remove a frame from the main window using the `forget()` method.
```python
root = tk.Tk()
root.title("Removing frame from the main window in Tkinter")
 
frame = tk.Frame(root, width=200, height=100, bg="blue")
frame.forget()
```
You can also use the `destroy()` method to destroy a frame and all its children. The difference between `forget()` and `destroy()` is that `forget()` removes the widget from the window but keeps it in memory, while `destroy()` removes the widget **permanently** from the window and frees up the memory.
```python
frame = tk.Frame(root, width=200, height=100, bg="blue")
frame.destroy()
```
* `Listbox` - a widget that displays a list of items. It can be used to display a list of options to the user. You can use the `insert()` method to add items to the listbox.
```python
# specify that only one item can be selected at a time
hof_gers = tk.Listbox(root, selectmode=tk.SINGLE)
hof_gers.pack()
 
for item in ["Laudrup", "McCoist", "Albertz", "Ferguson"]:
    # insert the item at the END of the listbox
    hof_gers.insert(tk.END, item)
```
* `Canvas` - a widget that can be used to draw shapes, images, and text. Tkinter does not support 3D graphics. For complex 3D graphics, libraries such as [PyOpenGL](https://pyopengl.sourceforge.net/) and [Visualisation Toolkit (VTK)](https://pypi.org/project/vtk/) would be more suitable.