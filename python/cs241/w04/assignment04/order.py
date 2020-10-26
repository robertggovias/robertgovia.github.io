from product import Product
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
        print("Order: ",self.id)
        print("{}\nSubtotal: ${:,.2f}\nTax: ${:,.2f}\nTotal: ${:,.2f}".format(self.print_product(),self.get_subtotal(),self.get_tax(),self.get_total()))