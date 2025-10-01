class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = 20000
emp = Employee('Jessa', 10000)
print('Salary:', emp._Employee__salary)  # Output: Salary: 20000

