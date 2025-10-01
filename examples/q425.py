class BankAccount:
    interest_rate = 0.05

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def calculate_interest(self):
        return self.balance * BankAccount.interest_rate

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
