class Person:   
    def __init__(self, age = 0):   
         self._age = age     
    def get_age(self):   
        return self._age       
    def set_age(self, a):   
        self._age = 20      
John = Person()        
John.set_age(19)   
print(John.get_age())
