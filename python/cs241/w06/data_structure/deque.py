from  collections import deque

pepe = deque([])
def prompt():
    name= input("name: ")
    pepe.append(name)
def display():
    print(pepe)
def questions():
    primera = "1. insertar: "
    segunda = "2. tirar: "
    tercera = "3. terminar"
    print("{}\n{}\n{}".format(primera, segunda, tercera))
questions()
option = int(input("chose one option: "))
while option != 3:
    if option == 1:
        prompt()
        display()
        questions()
        option = int(input("chose one option: "))
    elif option == 2:
        x=pepe.popleft()
        print("ahora estamos atendiendo a: {}".format(x))
        questions()
        option = int(input("chose one option: "))
    else:
        print("anser must be between 1 and 3")
        questions()
        prompt()

