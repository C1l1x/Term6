'''
2.  	Създайте клас BankAccount, който представлява банкова сметка, имаща като атрибути: accountNumber, 
name (име на собственика на акаунта като низов тип), баланс.

2.1.	Създайте конструктор с параметри

2.2.	Създайте метод deposit(), който управлява действията за депозит.

2.3.	Създайте метод withdrawal(), който управлява действията за теглене.

2.4.	Създайте метод bankFees(), за да приложите банковите такси с процент от 5% от балансовата сметка.

2.5.	Създайте метод display() за показване на подробности за акаунта.
'''

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
                
        
    def deposit(self, amount):
        self.balance += amount
        self.bankFees()
        print(f"You have been deposit {amount} in your bank account.")

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bankFees()
            print(f"You have withdrawal {amount} from your bank account.")

    def display(self):
        print(f"Account number: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


account = BankAccount("000000001", "Jhon Doe", 500)
account.display()
account.deposit(300)
account.display()
account.withdrawal(50)
account.display()
    
        
        
