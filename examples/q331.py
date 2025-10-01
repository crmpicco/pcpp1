class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            raise ValueError("Balance cannot be negative.")

    balance = property(get_balance, set_balance)
