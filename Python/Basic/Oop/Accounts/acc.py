class Accounts:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = file.read()
            self.balance = int(self.balance)
            print(self.balance)

    def withdraw(self, ammount):
        self.balance = self.balance - ammount
        print(self.balance)

    def deposit(self, ammount):
        self.balance = self.balance + ammount
        print(self.balance)

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Transfer(Accounts):
    def __init__(self, filepath):
        Accounts.__init__(self, filepath)
        fee = 5
        self.fee = fee

    def mokal(self, ammount):
        self.balance = self.balance - ammount - self.fee
        print(self.balance)

trans = Transfer('balance.txt')
trans.mokal(10)
