class Order:    
    def __init__(self):
        self.id = ""
        self.products = []
        self.name= ""        
        
    
    #def get_order_count(self):
    #    return self.
    
    def get_subtotal(self):
        return sum(self.products)
    def get_tax(self):
        return int(Order.get_subtotal * 6.5)

    def get_total(self):
        pass
    def add_order(self):   
        pass

    def display_summary(self):
        print("{} ({}) - {}".format(Order.get_subtotal(self),self.id,self.name))
newOrder = Order()
newOrder.id=31
newOrder.products = [14,2314,3143,13,24,3241]
newOrder.name = "Robert"

Order.display_summary(newOrder)
