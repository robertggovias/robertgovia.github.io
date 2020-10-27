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
        sum_of_orders = 0
        for final_totals in self.orders:            
            sum_of_orders += final_totals.get_total()             
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
        for order in self.orders:
            if self.get_order_count() > 1:
                print()
            order.display_receipt()
            

            
    
    def display_summary(self):
        '''
        Print each customer, and its orders (with products)
        '''
        print("Summary for customer '{}':\nName: {}".format(self.id,self.name))
        print("Orders:",self.get_order_count())
        print("Total: ${:.2f}".format(self.get_total()))

    def display_receipts(self):
        '''
        getting advance from all the other display functions, this one will print in detail all the details of the sale
        '''
        print("Detailed receipts for customer '{}':\nName: {}".format(self.id,self.name))
        if self.get_order_count() < 2:
            print()

        self.print_orders()