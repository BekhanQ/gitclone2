class Bank:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance


class ExtendedBank(Bank):
    def __init__(self, initial_balance, loan_limit):
        super().__init__(initial_balance)
        self._loan_limit = loan_limit

    def get_loan_limit(self):
        return self._loan_limit

    def set_loan_limit(self, new_limit):
        self._loan_limit = new_limit

    #property
    def balance(self):
        return self.get_balance()

    #balance.setter
    def balance(self, new_balance):
        self.set_balance(new_balance)

    #property
    def loan_limit(self):
        return self.get_loan_limit()

    #loan_limit.setter
    def loan_limit(self, new_limit):
        self.set_loan_limit(new_limit)


if __name__ == "__main__":
    bank = ExtendedBank(initial_balance=1000, loan_limit=5000)

    print("Before changes:")
    print("Balance:", bank.balance)
    print("Loan limit:", bank.loan_limit)

    # Изменение аргументов через property
    bank.balance = 1500
    bank.loan_limit = 6000

    print("\nAfter changes:")
    print("Balance:", bank.balance)
    print("Loan limit:", bank.loan_limit)
