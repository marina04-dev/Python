# Bank Account Class: exercise 10
class Person:
    def __init__(self, full_name, age, id_number):
        self.full_name = full_name
        self.age = age
        self.id_number = id_number
                
        
class Account:
    def __init__(self, number, owner, amount):
        self.number = number
        self.owner = owner
        self.amount = amount 
        
    def transfer_to(self, account, amount):
        if amount <= self.amount:
            self.amount -= amount
            account.amount += amount
            print(self.owner.full_name + " transfered " + str(amount) + " to " + account.owner.full_name)
        else:
            print("Not Enough Credit!")
        
        
p1 = Person("Bob Hope", "dead", "5757668686")
p2 = Person("Donald Trum", 75, "666575646")
        
        
a1 = Account("1253653646476767", p1, 12345655.23)
a2 = Account("646565575887876", p2, 56454635654555436.99)
a1.transfer_to(a2, 100000)

