class X:
    def message(self):
        print('Hello from class X')

class Y(X):
    def message(self):
        print('Hello from class Y')

class Z(X):
    def message(self):
        print('Hello from class Z')

class W(Y, Z):
    pass

print(W.__mro__)
