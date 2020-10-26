from product import Product
class Order:
    def __init__(self):
        '''
        Construct new orders just with the idea, and the list of profucts 
        '''
        self.id=""        
        self.products = []
    
    def add_product(self,add_new):
        '''
        this append each new product to create a list of products
        '''
        self.products.append(add_new)
    
    def get_subtotal(self):
        '''
        Through this list of products we can reach the total price of the product construted on the Product module.
        '''
        counting = 0
        sum_of_products = 0
        for totals in self.products:        
            totals = self.products[counting].get_total_price()
            sum_of_products += totals
            counting += 1        
        return sum_of_products

    def print_product(self):
        '''
        To print all the details of the product we iterate over the list to print each time the quick details of the products
        '''
        counting_products = 0
        for products_display in self.products:
            products_display = self.products[counting_products].display()
            counting_products += 1
        return products_display

    def get_tax(self):
        '''
        to get the tax from the sum of all the objects from product 

        '''
        tax = Order.get_subtotal(self) * 0.065
        return tax
    
    def get_total(self):
        '''
        finally the big total of one order including taxes
        '''
        total = Order.get_subtotal(self) + Order.get_tax(self)
        return total        
    
    def display_receipt(self):
        '''
        A brief of the orders will be printed here
        '''
        print("Order: ",self.id)
        print(self.print_product())       
        print("Subtotal: ${:,.2f}\nTax: ${:,.2f}\nTotal: ${:,.2f}".format(self.get_subtotal(),self.get_tax(),self.get_total()))