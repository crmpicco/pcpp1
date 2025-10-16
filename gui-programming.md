# GUI Programming

## Tkinter

### Events
`<Key>` is a special event triggered when any key is pressed. It can be used to bind a function to a key press event.

`<Button-1>` is a special event triggered when the left mouse button is clicked. It can be used to bind a function to a mouse click event.

`<Button-2>` is a special event triggered when the middle mouse button is clicked. It can be used to bind a function to a mouse click event.

`<Button-3>` is a special event triggered when the right mouse button is clicked. It can be used to bind a function to a mouse click event.

`<Motion>` is a special event triggered when the mouse is moved with a mouse button being held down. It can be used to bind a function to a mouse movement event.

Event handlers interact with various components to capture and transform user input. To add an event handler to a widget, you can use the `bind()` method of the widget. The `bind()` method takes two arguments: the event type and the function to be called when the event occurs.

### Widgets
Widgets create the components of the user interface

### Geometry Managers
| Geometry Manager | Description                                                                                                             | Typical Use Case                                                     | Key Methods / Options                                                |
|------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| `pack()`         | Organises widgets in **blocks** before placing them in the parent. Widgets are placed **top, bottom, left, or right**.  | Simple layouts like toolbars, sidebars, or stacking buttons.         | `side`, `fill`, `expand`, `padx`, `pady`                             |
| `grid()`         | Organises widgets in a **table-like grid** of rows and columns. Each cell can hold a widget.                            | Forms, dashboards, spreadsheet-like layouts.                         | `row`, `column`, `rowspan`, `columnspan`, `sticky`, `padx`, `pady`   |
| `place()`        | Places widgets at **absolute positions** or **relative positions** in a two-dimensional grid using x and y coordinates. | Precise control, overlays, or when you need pixel-perfect placement. | `x`, `y`, `relx`, `rely`, `width`, `height`, `relwidth`, `relheight` |
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
You can get the mouse cursor's coordinates from the event object by accessing the `x` and `y` properties of the event object, e.g.
```python
def click_icon(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")
```
#### Styling
`background` or `bg` - the background colour of the widget

`selectforeground` - the colour of the text when selected

`activebackground` - the background colour of the widget when it is active/under the cursor

tkinter does not provide a method for creating RGB colours directly. Colours in tkinter are usually represented with Hexadecimal colour codes, predefined colour names or custom colours.


- `Entry` - a single-line text input field. It can be used to get user input.

- `entry.insert()` - used to insert text into the entry field at a specific position or set an initial value

```python
entry.insert(0, "Please enter your name")
entry.insert(5, "*****")
# the Entry widget will display "Pleas*****e enter your name".
entry.get() # to retrieve the text entered by the user. Returned as a string.
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
* `Canvas` - a widget that can be used to draw shapes, images, and text in a window. Tkinter does not support 3D graphics. For complex 3D graphics, libraries such as [PyOpenGL](https://pyopengl.sourceforge.net/) and [Visualisation Toolkit (VTK)](https://pypi.org/project/vtk/) would be more suitable.

| Widget        | Description                                  | Clickable?                       |
|---------------|----------------------------------------------|----------------------------------|
| `Button`      | Standard clickable button                    | ✅                                |
| `Checkbutton` | Checkbox that can be toggled                 | ✅                                |
| `Radiobutton` | Radio button for selecting options           | ✅                                |
| `Label`       | Text/image display (can be made clickable)   | ⚠️ Indirect (with event binding) |
| `Entry`       | Single-line text input                       | ✅                                |
| `Text`        | Multi-line text input                        | ✅                                |
| `Scale`       | Slider for numeric values                    | ✅                                |
| `Spinbox`     | Entry widget with increment/decrement arrows | ✅                                |
| `Listbox`     | Displays a list of selectable items          | ✅                                |
| `Canvas`      | Drawing area (clickable with bindings)       | ⚠️ Indirect (with event binding) |
| `Menu`        | Dropdown or context menu                     | ✅                                |
| `Menubutton`  | Button that displays a menu                  | ✅                                |
| `Scrollbar`   | Scroll bar for scrolling                     | ✅                                |
| `PanedWindow` | Resizable container pane                     | ⚠️ Indirect                      |
| `Toplevel`    | Separate window                              | ⚠️ Indirect (window clicks)      |
| `Frame`       | Container widget                             | ❌                                |
| `LabelFrame`  | Container with a label                       | ❌                                |
| `Message`     | Display a block of text                      | ❌                                |
| `OptionMenu`  | Dropdown menu                                | ✅                                |

`StringVar` - a special variable that can be used to store a string value. It is used to store the value of a widget, such as an `Entry` or a `Label`. It can be used to get and set the value of a widget.

:information_source: You need to associate a `StringVar` with a widget to make it work. For example, you can associate a `StringVar` with an `Entry` widget to get the value of the entry field, or at the very least the master widget (e.g. the `Tk()` root window)

For example, this would throw an error because the `StringVar` is not associated with any widget:
```python
import tkinter as tk

rrp = tk.StringVar()
rrp.set("I have come here to chew bubble gum and kick ass, and I'm all out of bubble gum")

window = tk.Tk()
window.mainloop()
```

`bind()` - used to bind a function to a particular event, e.g.
```python
def on_button_click(event):
    print("Button clicked!")
    
button = tk.Button(root_window, text="Click Me")
button.bind("<Button-1>", on_button_click)
```
## messagebox
There are eight types of messageboxes:
1. showinfo
2. showwarning
3. showerror
4. askquestion
5. askokcancel
6. askretrycancel
7. askyesno
8. askyesnocancel

Messages boxes are modal and will return a subset of (True, False, OK, None, Yes, No) based on the user's selection