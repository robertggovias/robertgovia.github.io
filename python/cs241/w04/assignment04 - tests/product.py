class Product:
    def __init__(self,id,name,price,quantity):
        self.id = str(id)
        self.name = name
        self.price = float(price)
        self.quantity = float(quantity)
    def get_total_price(self):
        total = self.price * self.quantity
        return total

    def display(self):
        print("{} ({}) - {}".format(self.name,self.quantity,Product.get_total_price(self)))