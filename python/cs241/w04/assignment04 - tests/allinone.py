class Product:
    def __init__(self,id="",name="",price=0,quantity=0):
        self.id = id
        self.name= name
        self.price = price
        self.quantity = quantity
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity
    def get_total_price(self):
        return self.price * self.quantity
    def get_as_list(self):
        self.list = [self.id,self.name,self.price,self.quantity,self.get_total_price()]
        return self.list
    def display(self):
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity,Product.get_total_price(self)))
class Order:
    def __init__(self):
        self.id=""        
        self.products = []
    def add_product(self,add_new):
        self.products.append(add_new)
    '''
    def display_price(self):
        print(self.product_price)   '''
    def get_subtotal(self):           
        total = 0
        for totals in self.products:
            total += totals.get_total_price()
        return total
    def print_product(self):
        for products_display in self.products:
            a=products_display.display()
        return a
    def get_tax(self):
        tax = Order.get_subtotal(self) * 0.065
        return tax
    def get_total(self):
        total = Order.get_subtotal(self) + Order.get_tax(self)
        return total        
    def display_receipt(self):
        print("Order: ",self.id)
        print(self.print_product())       
        print("Subtotal: ${:.2f}\nTax: ${:.2f}\nTotal: ${:.2f}".format(self.get_subtotal(),self.get_tax(),self.get_total()))
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
        for final_totals in self.orders:
            final_totals.get_total()         
        return final_totals.get_total()
    def get_order_count(self):
        amount = len(self.orders)
        return amount
    def print_orders(self):        
        for order in self.orders:
            order.display_receipt()
    def display_summary(self):
        print("Summary for customer '{}':\nName: {}".format(self.id,self.name))
        print("Orders: ",self.get_order_count())
        print("Total: ${:.2f}".format(self.get_total()))
    def display_receipts(self):
        print("Detailed receipts for customer '{}':\nName: {}\n".format(self.id,self.name))
        print(self.print_orders())
'''
File: main.py
Author: Br. Burton
This file tests the customer, order, and product classes for
assignment 04. You should not need to change this file.
'''
def main():
    print("### Testing Products ###")
    p1 = Product("1238223", "Sword", 1899.99, 10)
    print("Id: {}".format(p1.id))
    print("Name: {}".format(p1.name))
    print("Price: {}".format(p1.price))
    print("Quantity: {}".format(p1.quantity))
    p1.display()
    print()
    p2 = Product("838ab883", "Shield", 989.75, 6)
    print("Id: {}".format(p2.id))
    print("Name: {}".format(p2.name))
    print("Price: {}".format(p2.price))
    print("Quantity: {}".format(p2.quantity))
    p2.display()
    print("\n### Testing Orders ###")
    # Now test Orders
    order1 = Order()
    order1.id = "1138"
    order1.add_product(p1)
    order1.add_product(p2)
    order1.display_receipt()
    print("\n### Testing Customers ###")
    # Now test customers
    c = Customer()
    c.id = "aa32"
    c.name = "Gandalf"
    c.add_order(order1)
    c.display_summary()
    print()
    c.display_receipts()
    # Add another product and order and display again
    p3 = Product("2387127", "The Ring", 1000000, 1)
    p4 = Product("1828191", "Wizard Staff", 199.99, 3)
    order2 = Order()
    order2.id = "1277182"
    order2.add_product(p3)
    order2.add_product(p4)
    c.add_order(order2)
    print()
    c.display_summary()
    print()
    c.display_receipts()
if __name__ == "__main__":
    main()