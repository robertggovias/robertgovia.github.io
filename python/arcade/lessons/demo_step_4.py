import arcade

WIDTH = 750
HEIGHT = 750
class SpaceShip:
    def __init__(self):
        self.y = 140
        self.x = 10
        self.dx = 10
        self.dy = 10
    
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,200, 453,arcade.color.GREEN)
    def fast(self):                
        if self.x > WIDTH:
            self.dx= self.dx * -1
        elif self.x <= 0:
            self.dx = self.dx * -1
        
        if self.y > HEIGHT:
            self.dy= self.dy * -1
        elif self.y <= 0:
            self.dy = self.dy * -1
        
        self.y += self.dy
        self.x += self.dx
 
class Aqui_puedo_escribir_lo_que_quiera(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.WHITE)
        self.ship = SpaceShip()        
        

    def on_draw(self):
        """
        Called every time we  need to draw the window :return:
        """
        arcade.start_render()
        self.ship.draw()
        
        
    
    def update(self, delta_time: float):
        """
        The purpose of this method is to move evertything foward.
        :param delta_time:
        :return:
        """
        

        self.ship.fast()
        
        pass

window = Aqui_puedo_escribir_lo_que_quiera(WIDTH,HEIGHT)
arcade.run()
    