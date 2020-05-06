class Ball:
    def __init__(self, radius = 0.0, color="Red"):
        self.radius = radius        
        self.color = color
    
    def static_function():
        print("pass")

if __name__=="__main__":
    my_ball= Ball(radius = 5.0, color="Blue")
    print("my radius is: ", my_ball.radius)
    print("my color is: ", my_ball.color)

    my_ball.static_function()
    Ball.static_function(my_ball)