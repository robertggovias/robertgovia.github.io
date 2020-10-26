from order import Order
from product import Product
class Customer:
    '''id=0
    price 
    quantity'''
    def __init__(self):
        self.id = ""
        self.name= ""
        self.orders = []
    
    def add_order(self,add_new):
        self.orders.append(add_new)
    
    def get_total(self):
        counting = 0
        sum_of_orders = 0
        for final_totals in self.orders:
            final_totals = self.orders[counting].get_total()
            sum_of_orders += final_totals
            counting += 1            
        return sum_of_orders
    
    def get_order_count(self):
        amount = len(self.orders)
        return amount
    
    def print_orders(self):
        counting_orders = 0
        for orders_display in self.orders:
            orders_display = self.orders[counting_orders].display_receipt()
            print(orders_display)
            counting_orders += 1
    
    def display_summary(self):
        print("Summary for customer '{}':\nName: {}".format(self.id,self.name))
        print("\nOrders: {}\nTotal: ${:,.2f}".format(self.get_order_count(),self.get_total()))

    def display_receipts(self):
        print("Detailed receipts for customer '{}':\nName: {}".format(self.id,self.name))
        print("\n{}\n".format(self.print_orders()))