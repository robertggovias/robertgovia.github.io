from order import Order

class Customer:
    '''id=0
    price 
    quantity'''
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name= name
        self.price = price
        self.quantity = quantity
        
    
    
    def get_total_price(self):
        return self.price * self.quantity

    def display(self):
        print("{} ({}) - ".format(self.price))
newCustomer = Customer(1,"robert",46,4)
Customer.display(newCustomer)