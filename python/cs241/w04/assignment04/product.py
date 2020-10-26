class Product:    
    def __init__(self,id="",name="",price=0,quantity=0):
        '''
        To construct objects with this four atributes:
        id
        name
        price
        quantity
        '''
        self.id = id
        self.name= name
        self.price = price
        self.quantity = quantity
        
    def get_total_price(self):
        '''
        multiply price by quanitty to get the total
        '''
        return self.price * self.quantity
        
    def display(self):
        '''
        This function just print all the attributes of the object (Except Id), not just because it will be done by main funciton, aslo because this is a resume.
        '''
        print("{} ({}) - ${:,.2f}".format(self.name, self.quantity,Product.get_total_price(self)))