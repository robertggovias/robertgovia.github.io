import arcade
class SpaceShip:
    def __init__(self):
        self.y = 10
        self.x = 10
    
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,200, 453,arcade.color.GREEN)
    def fast(self):
        self.y += 10
        self.x += 10
 
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

window = Aqui_puedo_escribir_lo_que_quiera(1000,1000)
arcade.run()
    