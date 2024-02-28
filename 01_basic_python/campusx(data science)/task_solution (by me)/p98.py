# Write code here
class Bill:

  def __init__(self,items,price):
    self.total = 0
    self.items = items
    self.price = price

    for i in self.price:
      self.total = self.total + i

  def display(self):
    print('Item \t\t\t Price')
    for i in range(len(self.items)):
      print(self.items[i],'\t',self.price[i])
    print("*"*10)

    print("Total",self.total)

class CashPayment(Bill):

  def __init__(self,items,price,deno,value):
    super().__init__(items,price)

    self.deno = deno
    self.value = value

  def show_cash_payment(self):
    super().display()
    for i in range(len(self.deno)):
      print(self.deno[i],"*",self.value[i],"=",self.deno[i]*self.value[i])

class ChequePayment(Bill):

  def __init__(self,items,price,cno,name):
    super().__init__(items,price)

    self.cno = cno
    self.name = name

  def show_cheque_payment(self):
    super().display()
    print('Cheque no',self.cno)
    print('Bank name',self.name)

items = ["External Hard Disk", "RAM", "Printer", "Pen Drive"]
price = [5000, 2000, 6000, 800]

deno = [10, 20, 50, 100, 500, 2000]
value = [1, 1, 1, 20, 4, 5]
cash = CashPayment(items, price, deno, value)
cash.show_cash_payment()

items = ["External Hard Disk", "RAM", "Printer", "Pen Drive"]
price = [5000, 2000, 6000, 800]
option = int(input("Would you like to pay by cheque or cash (1/2): "))

if option == 1:
    name = input("Enter the name of the bank: ")
    cno = input("Enter the cheque number: ")
    cheque = ChequePayment(items, price, cno, name)
    cheque.show_cheque_payment()

else:
    deno = [10, 20, 50, 100, 500, 2000]
    value = [1, 1, 1, 20, 4, 5]
    cash = CashPayment(items, price, deno, value)
    cash.show_cash_payment()



items = ["External Hard Disk", "RAM", "Printer", "Pen Drive"]
price = [5000, 2000, 6000, 800]

deno = [10, 20, 50, 100, 500, 2000]
value = [1, 1, 1, 20, 4, 5]
cash = CashPayment(items, price, deno, value)
cash.show_cash_payment()

items = ["External Hard Disk", "RAM", "Printer", "Pen Drive"]
price = [5000, 2000, 6000, 800]
option = int(input("Would you like to pay by cheque or cash (1/2): "))

if option == 1:
    name = input("Enter the name of the bank: ")
    cno = input("Enter the cheque number: ")
    cheque = ChequePayment(items, price, cno, name)
    cheque.show_cheque_payment()

else:
    deno = [10, 20, 50, 100, 500, 2000]
    value = [1, 1, 1, 20, 4, 5]
    cash = CashPayment(items, price, deno, value)
    cash.show_cash_payment()

    