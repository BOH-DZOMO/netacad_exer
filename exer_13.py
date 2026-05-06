class BankAccount():
    def __init__(self,owner, balance=0.0):
        self.owner = owner
        self._balance = balance

    def __str__(self):
        return f"Account: {self.owner} balance: {self._balance}"
    
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"
    
    def deposit(self, amount):
        self._balance += amount
    
    def  withdraw(self,amount):
        diff = self._balance - amount
        if diff <0 :
            raise ValueError("yes")
        self._balance -= amount
    
    

account1 = BankAccount("bob",100_000)
account1.deposit(10_000)
print(repr(account1))
account1.withdraw(130000)