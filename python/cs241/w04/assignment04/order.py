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
        total = 0
        for totals in self.products:
            total += totals.get_total_price()
        return total

    def print_product(self):
        '''
        To print all the details of the product we iterate over the list to print each time the quick details of the products
        '''        
        for products_display in self.products:
            products_display.display()                    

    def get_tax(self):
        '''
        to get the tax from the sum of all the objects from product 
        '''
        return Order.get_subtotal(self) * 0.065
    
    def get_total(self):
        '''
        finally the big total of one order including taxes
        '''
        return  Order.get_subtotal(self) + Order.get_tax(self)
    
    def display_receipt(self):
        '''
        A brief of the orders will be printed here
        '''
        print("Order:",self.id)
        Order.print_product(self)
        print("Subtotal: ${:.2f}\nTax: ${:.2f}\nTotal: ${:.2f}".format(self.get_subtotal(),self.get_tax(),self.get_total()))