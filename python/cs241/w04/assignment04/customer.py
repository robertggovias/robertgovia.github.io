from order import Order
from product import Product
class Customer:
    '''id=0
    price 
    quantity'''
    def __init__(self):
        '''
        Construction of an empty object to receive the id from the customer, and his name. Then will receive the list of orders
        '''
        self.id = ""
        self.name= ""
        #this empty list will receive all new order
        self.orders = []
    
    def add_order(self,add_new):
        '''
        Each time a new object of th class order is created will be appended on this line.
        '''
        self.orders.append(add_new)
    
    def get_total(self):
        '''
        The last code create a list, but we need to iterate on each element to get from each one de return of the funciton get_total from the class order.

        '''
        counting = 0
        sum_of_orders = 0
        for final_totals in self.orders:
            final_totals = self.orders[counting].get_total()
            sum_of_orders += final_totals
            counting += 1            
        return sum_of_orders
    
    def get_order_count(self):
        '''
        as easy as qwe have a list, to know the quantity of member of taat list we will use  -len - which will evaluate how long is the list
        '''
        amount = len(self.orders)
        return amount
    
    def print_orders(self):
        '''
        To print each order, we iterate on each element and print each one with its display code.
        '''
        counting_orders = 0
        for orders_display in self.orders:
            orders_display = self.orders[counting_orders].display_receipt()
            print(orders_display)
            print("")
            counting_orders += 1
    
    def display_summary(self):
        '''
        Print each customer, and its orders (with products)
        '''
        print("Summary for customer '{}':\nName: {}".format(self.id,self.name))
        print("Orders: ",self.get_order_count())
        print("Total: ${:,.2f}".format(self.get_total()))

    def display_receipts(self):
        '''
        getting advance from all the other display functions, this one will print in detail all the details of the sale
        '''
        print("Detailed receipts for customer '{}':\nName: {}\n".format(self.id,self.name))
        print(self.print_orders())