class Bank:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance


class ExtendedBank(Bank):
    def __init__(self, initial_balance, loan_limit, interest_rate):
        super().__init__(initial_balance)
        self._loan_limit = loan_limit
        self._interest_rate = interest_rate

    def get_loan_limit(self):
        return self._loan_limit

    def set_loan_limit(self, new_limit):
        self._loan_limit = new_limit

    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, new_rate):
        self._interest_rate = new_rate

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

    #property
    def interest_rate(self):
        return self.get_interest_rate()

    #interest_rate.setter
    def interest_rate(self, new_rate):
        self.set_interest_rate(new_rate)


if __name__ == "__main__":
    # Создаем экземпляр класса ExtendedBank
    bank = ExtendedBank(initial_balance=1000, loan_limit=5000, interest_rate=0.05)

    # Выводим начальные значения атрибутов
    print("Before changes:")
    print("Balance:", bank.balance)
    print("Loan limit:", bank.loan_limit)
    print("Interest rate:", bank.interest_rate)

    # Изменяем аргументы через property
    bank.balance = 1500
    bank.loan_limit = 6000
    bank.interest_rate = 0.04

    # Выводим значения атрибутов после изменений
    print("\nAfter changes:")
    print("Balance:", bank.balance)
    print("Loan limit:", bank.loan_limit)
    print("Interest rate:", bank.interest_rate)
