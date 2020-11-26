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


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

initial_velocity = random.uniform(-2, 2)
# This initial position garanteed that even the height of the screen is changed, the ball will always be in inside the screen
initial_position = random.uniform(0, SCREEN_HEIGHT)

class Point:
    '''The default initial position x = 0 will help the ball to emerge from the left, meanwhile the paddle will overwrite this default to start on the right of the screen
    '''
    def __init__(self):
        self.x = 0
        self.y = initial_position

class Velocity:
    '''
    The random.uniform works for both x and y velocity
    '''
    def __init__(self):
        self.dx = initial_velocity
        self.dy = initial_velocity

class Ball:
    '''
    the ilusion of moving ball which move alone, is change its position in a conditional loop summing up the cordinates x and y values.
    '''
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x,self.center.y,BALL_RADIUS,arcade.color.GREEN)
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    '''
    The behaviour that result from an impact is the opose of the velocity, in other words the negative.
    '''        

    def bounce_horizontal(self):
        self.velocity.dx = -(self.velocity.dx)
        self.center.x += self.velocity.dx       
    def bounce_vertical(self):
        self.velocity.dy = -(self.velocity.dy)
        self.center.y += self.velocity.dy

    def restart(self):
    # At the moment the best way to garanted a random velocity and position is to ask again to random perform a new random number, because using de same variable had been returning always the same starting position and velocity

        self.velocity.dy = random.uniform(-2, 2)
        self.velocity.dx = random.uniform(-2, 2)
        self.center.x = 0
        self.center.y = random.uniform(0, 200)


class Paddle:
    def __init__(self):
        self.center=Point()
        self.center.y = 45
        self.center.x = 380

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y ,PADDLE_WIDTH,PADDLE_HEIGHT,arcade.color.GREEN)
        
    def move_up(self):
        '''
        To make a vertical move it just needed to be changed the y cordinate (self.center.y).
        To avoid going out the vertical bunders the move_up it's only allowed with the condition to be less of the height of the screen, and also less than the middle of the height of the paddle
        '''        
        if self.center.y < SCREEN_HEIGHT - PADDLE_HEIGHT/2:
            self.center.y += MOVE_AMOUNT
        
    def move_down(self):
        '''
        To avoid going out the vertical bunders the move_down it's only allowed with the condition to be more of 0, and also more than the middle of the height of the paddle
        '''

        if self.center.y > 0 + PADDLE_HEIGHT/2:
            self.center.y -= MOVE_AMOUNT





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

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
                    abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                    self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False

# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()