import datetime

class Product:
    def __init__(self):
        self.manufacturing_date = input('enter manufacturing date (MM/DD/YYYY)')
        self.expiry_date = input('enter EXPIRY date (MM/DD/YYYY)')

        self.manufacturing_date = datetime.datetime.strptime(self.manufacturing_date, '%m/%d/%Y')
        self.expiry_date = datetime.datetime.strptime(self.expiry_date, '%m/%d/%Y')
     


    def time_to_expire(self):
        # Calculate the time difference between today's date and the expiry date
        today =  datetime.datetime.now()

        if today > self.expiry_date:
            print('mal expire ho gya')
        else:
            time_left = self.expiry_date.date() - today.date()    
            print(time_left)


obj = Product()
obj.time_to_expire()
