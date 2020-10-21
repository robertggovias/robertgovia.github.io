

class Product:
    '''id=0
    price 
    quantity'''
    def __init__(self,id,name,price,quantity):
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
        print("{} ({}) - ${:,.2f}".format(self.name, self.quantity,Product.get_total_price(self)))
#p1 = Product(1,"crema e nata",46.234,4)
#p2 = Product(2,"bolo de nata",536.555,7)
#Product.display(p1)
#Product.display(p2)
#print(p2.get_as_list())