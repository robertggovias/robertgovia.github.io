class Robot:
    def __init__(self, x_coordinate, y_coordinate, fuel_amount):
        self.x = x_coordinate
        self.y = y_coordinate
        self.fuel = fuel_amount
    '''def get_x (self):
        return self.x
    
    def get_y (self):
        return self.y
    
    def get_fuel (self):
        return self.x'''
    
    def get_status(self):
        status = print("({},{}) - Fuel: {}\n".format(self.x,self.y,self.fuel))#,str(self.x),",",str(self.y),") - Fuel: ",str(self.fuel))
        #status = print("(",self.x,",",self.y,") - Fuel: ",self.fuel)
        return status

    def prompt_command(self):
        while self.fuel > -11:
            command = input("Enter command: ")

            if command == "left":
                if self.fuel - 5 < 0:
                    print("Insufficient fuel to perform action")
                else:
                    self.x -= 1                
                    self.fuel -= 5
            elif command == "right":
                if self.fuel - 5 < 0:
                    print("Insufficient fuel to perform action")
                else:                    
                    self.x += 1                
                    self.fuel -= 5
                
            elif command == "down":
                if self.fuel - 5 < 0:
                    print("Insufficient fuel to perform action")
                else:    
                    self.y += 1
                    self.fuel -= 5
                    
            elif command == "up":
                if self.fuel - 5 < 0:
                    print("Insufficient fuel to perform action")
                else:
                    self.y -= 1
                    self.fuel -= 5
                    
            elif command == "fire":
                if self.fuel - 15 < 0:
                    print("Insufficient fuel to perform action")
                else:
                    self.fuel -= 15
                    print("Pew! Pew!")
                
            elif command == "status":                        
                print("({}, {}) - Fuel: {}".format(self.x,self.y,self.fuel))
            elif command == "quit":
                print("Goodbye.")
                break

            #else:
             #   print("command optios are: Left, Rigth, Up,. Down, Fire and status")

        return Robot(self.x, self.y, self.fuel)

start = Robot(10,10,100)
'''
def prompt_status():
    command = input("Enter command: ")
    status = Robot(input("oi: "),input("oi: "), input("oi: "))
    return Robot.get_status(start)'''

def main():
    Robot.prompt_command(start)    

if __name__ == "__main__":
    main()