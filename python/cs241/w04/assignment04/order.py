from product import Product
class Order:
    def __init__(self):
        self.order_Id=""        
        self.products = []
    
    def get_id(self):
        return self.order_Id

    def get_products(self):
        return self.products
    
    def display_test(self):
        print("products{}".format(Order.get_products(self)))

    def get_subtotal(self):
        return Product.get_total_price(self)
    
    def get_tax(self):
        return 0,65*Order.get_subtotal(self)
    def get_total(self):
        return Order.get_subtotal(self) + Order.get_tax(self)
        
    def add_product(self,p1):
        self.products.append(p1)
    
    def display_receipt(self):
        print("Order: {}\n{}\nSubtotal: ${:,.2f}\nTax: ${}\nTotal: ${:,.2f}".format(self.order_Id,Product.display(self),self.get_subtotal(),self.get_tax(),self.get_total()))



sim = Order()
sim.order_Id = 3
sim.products = 6.65
Order.get_subtotal(sim)
#Order.display_receipt(sim)
#Order.get_subtotal(sim)