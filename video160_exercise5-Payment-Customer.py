class Customer:
    def __init__(self,fullname,address,orders=None):
        self.fullname = fullname
        self.address = address
        if orders is None:
            self.orders = []
        else:
            self.orders = orders
        
    def place_order(self,order):
        self.orders += [order]
        
    def __str__(self):
        st = f"Fullname: {self.fullname}, Address: {self.address}"
        st += "\n" + "-" * 45
        s = 0 
        for order in self.orders:
            st += "\n" + str(order)
            s += order.payment.amount
        st += "\n" + "-" * 45
        st += f"\nTotal: {s}" 
        return st 
        
        
class Order:
    def __init__(self, date, payment):
        self.date = date
        self.payment = payment
        
    def __str__(self):
        return f"Date: {self.date} \nPayment: {self.payment} "
        
class Payment:
    def __init__(self, amount):
        self.amount = amount
        
    def __str__(self):
        return str(self.amount)
      
      
class Credit(Payment):
    def __init__(self, amount, number, exp_date):
        super().__init__(amount)
        self.number = number 
        self.exp_date = exp_date
        
    def __str__(self):
        return super().__str__() + f"\nCredit: \n Number: {self.number}\n Exp.Date: {self.exp_date}"
        
        
class Check(Payment):
    def __init__(self,amount, number, bank_code):
        super().__init__(amount)
        self.number = number
        self.bank_code = bank_code
        
    def __str__(self):
        return super().__str__() + f"\nCheck: \n Number: {self.number}\n Bank Code: {self.bank_code}"
        


    
def main():
    c = Customer("Jim Carlos", "New York,33456")
    c.place_order(Order("2020-08-12", Payment(12.23)))
    c.place_order(Order("2020-08-20", Credit(33.66, "66665565-7778", "2020-12-23")))
    c.place_order(Order("2020-08-30", Check(40.23, "6335453453-2211", "5678856-878/3")))
    print(c)
    
main()
