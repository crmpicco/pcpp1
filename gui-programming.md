# GUI Programming

## Tkinter

### Events
`<Key>` is a special event that is triggered when any key is pressed. It can be used to bind a function to a key press event.

`<Motion>` is a special event that is triggered when the mouse is moved with a mouse button being held down. It can be used to bind a function to a mouse movement event.

### Widgets

- `Entry` - a single-line text input field. It can be used to get user input. 
```python
entry.insert(0, "Please enter your name")
entry.insert(5, "*****")
# the Entry widget will display "Pleas*****e enter your name".
```
