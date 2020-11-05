class Product:
    def __init__(self):
        self.price = 0.0
        self.quantity = 0

    def get_total_price(self):
        return self.price * self.quantity

class Cereal(Product):
    def __init__(self):
        
        #First call the base call version        
        super().__init__()

        #Now setup any number of variables
        self.weight= 0.0

    def calculate_shipping_cost(self):
        return 0.05 * self.weight
    
cornflakes = Cereal()
cornflakes.price = 32
cornflakes.weight = 1
cornflakes.quantity = 4
print(cornflakes.get_total_price()+cornflakes.calculate_shipping_cost())
