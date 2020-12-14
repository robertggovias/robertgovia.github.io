"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

OBJECT_HIDING = 45
INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_SPEED = BIG_ROCK_SPEED + 3.5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point:
    def __init__(self):
        self.x = 0.00
        self.y = 0.00
class Center(Point):
    def __init__(self):
        super().__init__()
        self.x = SCREEN_WIDTH / 2
        self.Y = SCREEN_HEIGHT / 2

class Dificulty:
    def __init__(self):
        self.magic_number = 1
        self.edx = self.magic_number 
        self.edy = self.magic_number
class Spin(arcade.Sprite):
    def update(self):
        super().__init__()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))
class Velocity():
    def __init__(self,x):
        self.dy = 1.00*x
        self.dx = 1.00*x

class FlyingObject_Base(Point):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.radius = 0
        self.velocity = 0
        self.angle = 0
        #self.texture = arcade.load_texture(self.img) 
    
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        if self.x >  self.SCREEN_WIDTH+OBJECT_HIDING:
            return True
        elif self.y > self.SCREEN_HEIGHT+OBJECT_HIDING:
            return True
        elif self.x < 0-OBJECT_HIDING:
            return True
        elif self.y < 0-OBJECT_HIDING:
            return True

class Asteroid(FlyingObject_Base):
    def __init__(self):
        super().__init__()
        self.asteroids = 0
        where= random.randint(1,4)
        if where == 1:
            self.x = random.randint(0,SCREEN_WIDTH)
            self.y = SCREEN_HEIGHT+OBJECT_HIDING
            self.angle = random.randint(225,315)
            print(self.x,self.y,self.angle)
        elif where == 2:
            self.x = random.randint(0,SCREEN_WIDTH)
            self.y = 0-OBJECT_HIDING
            self.angle = random.randint(45,135)
            print(self.x,self.y,self.angle)
        elif where == 3:        
            self.x = 0-OBJECT_HIDING
            self.y = random.randint(0,SCREEN_HEIGHT)
            up_down = random.randint(1,2)
            if up_down == 1:
                self.angle = random.randint(0,45)
            elif up_down == 2:
                self.angle = random.randint(315,360)
            print(self.x,self.y,self.angle)
        elif where == 4:        
            self.x = SCREEN_WIDTH+OBJECT_HIDING
            self.y = random.randint(0,SCREEN_HEIGHT)
            self.angle = random.randint(135,225)
            print(self.x,self.y,self.angle)
        
        self.velocity = Velocity(BIG_ROCK_SPEED) 
        self.radius = BIG_ROCK_RADIUS                        
        
        self.turn = 1 

    def hit(self):
        return 1
    def draw(self):
        img = "images/meteorGrey_big1.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        self.turn += BIG_ROCK_SPIN
        arcade.draw_texture_rectangle(self.x,self.y,width,height,texture,self.turn,255)        
        
    def advance(self):
        self.dificulty = Dificulty()            
        self.x += math.cos(math.radians(self.angle)) * self.velocity.dx * self.dificulty.edx
        self.y += math.sin(math.radians(self.angle)) * self.velocity.dy * self.dificulty.edy              

class Asteroid_Medium(Asteroid):
    def __init__(self):
        super().__init__()
        self.velocity = Velocity(MEDIUM_ROCK_SPEED) 
        self.radius = MEDIUM_ROCK_RADIUS 
    def draw(self):
        img = "meteorGrey_med1.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height 
        self.turn += MEDIUM_ROCK_SPIN
        arcade.draw_texture_rectangle(self.x,self.y,width,height,texture,self.turn,255)        

       
class Ship(FlyingObject_Base):
    def __init__(self):
        self.radius = SHIP_RADIUS
        self.center = Center()
        self.x = self.center.x
        self.y = self.center.y        
    
    def draw(self):
        '''
        img = "images/playerShip1_orange.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent        
        arcade.draw_texture_rectangle(self.x, self.y, width, height, texture, 0, alpha)
        '''

    
    def advance(self):
        pass
class Bullet(FlyingObject_Base):
    def __init__(self):
        super().__init__()        
        self.radius = BULLET_RADIUS
        self.img = "images/laserBlue01.png"        
        self.center = Center()

    def draw(self):
        texture = arcade.load_texture(self.img)

        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent        
        self.x = self.center.x
        self.y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(self.x, self.y, width, height, texture, angle, alpha)
    
    def advance(self):
        pass
    

    pass
def backTexture(texture):    
    back_img = texture
    texture_back = arcade.load_texture(back_img)
    arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,texture_back,0,255)   

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """
    

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        

        self.background = None
        

        arcade.set_background_color(arcade.color.BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship= Ship()
        self.score = 0
        self.asteroids = []
        self.bullets = []

    

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        # clear the screen to begin drawing
        arcade.start_render()
        
        backTexture("images/back_star.jpg")
        """texture_back = arcade.load_texture(back_img)
        arcade.draw_texture_rectangle(0,0,800,600,texture_back,0,255)"""

        self.ship.draw()
        for bullet in self.bullets:
            bullet.draw()
        
        for asteroid in self.asteroids:
            asteroid.draw()

        self.draw_score()
    
    def draw_score(self):
        """
        Puts the current score on the screen
        """
        
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE_SMOKE)
        
        
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions
        self.check_collisions()
        self.check_off_screen()
        # decide if we should start a asteroid
        if random.randint(1, 50) == 1:
            self.create_asteroid()
        for asteroid in self.asteroids:
            asteroid.advance()
        for bullet in self.bullets:
            bullet.advance()
        # TODO: Iterate through your asteroids and tell them to advance
   
    def create_asteroid(self):
        """
        Creates a new asteroid of a random type and adds it to the list.
        :return:
        """
        # TODO: Decide what type of asteroid to create and append it to the list
        while len(self.asteroids) < INITIAL_ROCK_COUNT:
            new_asteroid = Asteroid()   
            self.asteroids.append(new_asteroid)
    
    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Updates scores and removes dead items.
        :return:
        """
        # NOTE: This assumes you named your asteroids list "asteroids"
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius
                    if (abs(bullet.center.x - asteroid.center.x) < too_close and abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        asteroid.alive = False
                        self.score += asteroid.hit()
                        # We will wait to remove the dead objects until after we
                        # finish going through the list
        # Now, check for anything that is dead, and remove it
        
        self.cleanup_zombies()
    def cleanup_zombies(self):
        """
        Removes any dead bullets or asteroids from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)
                print("asteroid_KILLED")
    def check_off_screen(self):
        """
        Checks to see if bullets or asteroids have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)
                print("a bullet has dissapeared")
        for asteroid in self.asteroids:
            if asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.asteroids.remove(asteroid)
                print("a asteroid has left the game")

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        

        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()