"""
File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random

# These are Global constants to use throughout the game
random.uniform(-2, 2)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Point:
    def __init__(self):
        self.x = random.uniform(-2, 500)
        self.y = random.uniform(-2, 500)

class Velocity:
    def __init__(self):
        self.dx = 0.00
        self.dy = 0.00

class Ball:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x,self.center.y,BALL_RADIUS,arcade.color.GREEN)
        
    def advance(self):
        pass

    def bounce_horizontal(self):
        pass
    def bounce_vertical(self):
        pass
    def restart(self):
        pass

class Paddle:
    def __init__(self):
        self.center=Point()

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y ,PADDLE_HEIGHT,PADDLE_WIDTH,arcade.color.GREEN)
    def move_up(self):
        pass
    def move_down(self):
        pass




class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()