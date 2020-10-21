from product import Product
class Order:
    def __init__(self):
        self.order_Id=""
        self.products = []
        self.price = Product.get_price
        self.quantity = Product.get_quantity    
    def add_product(self):
        self.products.append(Product.get_as_list(self))   
        
    def get_products(self):        
        return self.products
    
#    def display_test(self):
#       print("products{}".format(Order.get_products(self)))


'''     
    def print_product_list(self):        
        print(Order.get_products(self))

    def product_count(self):
        many_products = len(self.products)
        print(many_products)

    def get_subtotal(self):
        return Product.get_total_price(self)
    
    def get_tax(self):
        return 0,65*Order.get_subtotal(self)
    def get_total(self):
        return Order.get_subtotal(self) + Order.get_tax(self)'''
    
    #def display_receipt(self):
    #    print("Order: {}\n{}\nSubtotal: ${:,.2f}\nTax: ${}\nTotal: ${:,.2f}".format(self.order_Id,Product.display(self),self.get_subtotal(),self.get_tax(),self.get_total()))
print("### Testing Products ###")
p1 = Product("1238223", "Sword", 1899.99, 10)
p2 = Product("1238223", "Sword", 1899.99, 2)
#p2 =Order()
Product.display(p1)
Product.display(p2)
print("Id: {}".format(p1.id))
print("Name: {}".format(p1.name))
print("Price: {}".format(p1.price))
print("Quantity: {}".format(p1.quantity))

p1.display()

print()
print("Id: {}".format(p1.id))
list2 = []
list2.append(p1.get_as_list())
list2.append(p2.get_as_list())
print(list2)

order1 = Order()
print(order1.get_products())
#Order.print_product_list(p1)
'''def main():
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


if __name__ == "__main__":
    main()'''

'''
sim = Order()
sim.order_Id = 3
sim.products = 6.65
Order.get_subtotal(sim)
#Order.display_receipt(sim)
#Order.get_subtotal(sim)'''