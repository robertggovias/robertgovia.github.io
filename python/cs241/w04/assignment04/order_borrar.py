from product import Product
from customer import Customer
class Order:
    def __init__(self):
        self.id=""        
        self.products = []
        
        
        #self.price = Product.get_price
        #self.quantity = Product.get_quantity

    def add_product(self,add_new):
        self.products.append(add_new)
    '''
    def display_price(self):
        print(self.product_price)   '''
   
    def get_subtotal(self):           
        counting = 0
        sum_of_products = 0
        for totals in self.products:        
            totals = self.products[counting].get_total_price()
            sum_of_products += totals
            counting += 1        
        return sum_of_products
    #def print_subtotal(self):
    #    print(Order.get_subtotal(self))

    def print_product(self):
        counting_products = 0
        for products_display in self.products:
            products_display = self.products[counting_products].display()
            counting_products += 1
        return products_display

    def get_tax(self):
        tax = Order.get_subtotal(self) * 0.065
        return tax
    
    def get_total(self):
        total = Order.get_subtotal(self) + Order.get_tax(self)
        return total
    
    #def print_tax(self):
    #    print(Order.get_tax(self))
        
    
    def display_receipt(self):
        print("Order: {}\n{}\nSubtotal: ${:,.2f}\nTax: ${}\nTotal: ${:,.2f}".format(self.id,self.print_product(),self.get_subtotal(),self.get_tax(),self.get_total()))
        
    
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
    print("\n\ndisplay test")
    print(p2.display())

    p2.display()
    # Now test Orders
    order1 = Order()
    order1.id = "1138"
    order1.add_product(p1)
    order1.add_product(p2)   
    order1.display_receipt()
    print("print poduct test")
    order1.print_product()

    


if __name__ == "__main__":
        main()