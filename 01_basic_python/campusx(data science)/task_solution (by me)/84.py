class bankAccount:
    def __init__(self, accountNumber, name, balance ):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def display(self):
        print('Account Number :',self.accountNumber)
        print('Account Name :',self.name)
        print('Account Balance :',self.balance,'₹')


    def deposit(self, deposit):
        
        self.balance = self.balance + deposit

        return print('amount deposited in bank now your current balance is ', self.balance)
    
    def withdrawl(self, withdrawl):
    
        if withdrawl < self.balance:
            
            self.balance = self.balance - withdrawl 
            reduction = self.bankfees()
            self.balance = self.balance - reduction

            return print('amount withdrwal from bank now your current balance is ', self.balance)
        else: 
            return print('chal futt yaha se')

    def bankfees(self):

        return self.balance*0.05


cust = bankAccount(1000000,'bhavya', 500)
cust.deposit(500)
cust.withdrawl(100)
cust.display()