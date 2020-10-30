import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Gets the folder to the current file
my_file = os.path.join(THIS_FOLDER, 'file.txt') # Generates the absolute path to the file
os.chdir(THIS_FOLDER)
# Open the file

lr=open("stacks01.txt","r")
print(lr.read())




pepe = [line.strip(" \n") for line in open("stacks06.txt")]
print(pepe)
#print("pepe",pepe)


# Read through it character by character
# One way to do this for this program, is to read line by line
# and then call line.strip() to get rid of any whitespace
#open(text_file)

new_list = []
count = 0
#colocar un def (funcion aquí para (despues de haber verificado stisfactoriamente si hay el de cierre correspondiente, verifique si hay uno de apertura)
for active in pepe:
    if "(" in active:
        hello = True
    elif "{" in active:
        hello = True
    elif "[" in active:
        hello = True
    else:
        break
        #hello = False
    if hello == True:
        new_list.append(active)
    count+=1
    print(count)
    print(new_list)

def opose(x,y):
    def oponent(x):
        if x == "[":
            comparr = "]"
        elif x == "{":
            comparr = "}"
        elif x == "(":
            comparr = ")"
        else:
            comparr = False
        return comparr
    print(oponent(x))
    
    if y == oponent(x):
        return ("match")
    else:
        return ("don't match")
#opose("{","}")
if  len(pepe)!=1:    
    while len(new_list) > 0:
        x=new_list[len(new_list)-1]
        print(x)
        y=pepe[count]    
        print(y)

        if opose(x,y) == ("match"):
            new_list.pop()
        else:
            print("Not balanced")
            break
        count+=1
        print(new_list)

    if pepe[count-1] == pepe[len(pepe)-1]:
        print("you did it men")
else:
    print("Not Banlanced")    
    
'''

    # If current character is any type of opening brace: (, {, [
        # push it (the current character) on to a stack

    # if current character is any type of closing brace: ), }, ]
        # compare it to the thing on the top of the stack
            # If the stack is empty (nothing to compare)
                # Quit now, it doesn't match
            # if they match (meaning closing of the same type):
                # We're good
                # Pop the opening brace off the stack
            # If they don't match
                # Quit now, and tell them the braces don't match
    
# after reading the complete file

# If there is anything on the stack, the braces didn't match'''