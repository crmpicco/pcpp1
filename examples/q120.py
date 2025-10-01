def html(func):
    def wrapper(*args, **kwargs):
        print("<html>")
        func(*args, **kwargs)
        print("</html>")
    return wrapper

def body(func):
    def wrapper(*args, **kwargs):
        print("<body>")
        func(*args, **kwargs)
        print("</body>")
    return wrapper

@html
@body
def text_printer(text):
    print(text)

text_printer("This is my text")
