from order import Order

class Customer:
    '''id=0
    price 
    quantity'''
    def __init__(self):
        self.id = ""
        self.name= ""
        self.orders = []
        
    
    def get_order_count(self):
        return len(self.orders)
    
    def get_total(self):
        return sum(self.orders)
        
    def add_order(self,c):
        self.orders.append(c)
    
    def display_summary(self):
        print("Summary for customer {}:\nName: {}\nOrders: {}\nTotal: ${:,.2f}".format(self.id,self.name,self.get_order_count(),self.get_total()))
    def display_receipts(self):
        print("Detailed receipts for customer {}:\nName: {}\n\n{}\n\n".format(self.id,self.name,Order.display_receipt(self)))
    
newCustomer = Customer()
Customer.display_summary(newCustomer)
newCustomer.add_order(4241)
newCustomer.add_order(4241)
newCustomer.add_order(4241)
newCustomer.add_order(4241)
print(Customer.get_order_count(newCustomer))
Customer.display_summary(newCustomer)
