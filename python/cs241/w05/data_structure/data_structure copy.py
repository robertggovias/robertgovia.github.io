import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Gets the folder to the current file
my_file = os.path.join(THIS_FOLDER, 'file.txt') # Generates the absolute path to the file
os.chdir(THIS_FOLDER)
# Open the file

lr=open("stacks03.txt","r")
print(lr.read())




pepe = [line.strip(" \n") for line in open("stacks03.txt")]
print(pepe)
#print("pepe",pepe)


# Read through it character by character
# One way to do this for this program, is to read line by line
# and then call line.strip() to get rid of any whitespace
#open(text_file)

new_list = []
count = 0
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
        
    if y == oponent(x):
        print("same")
    else:
        print("errorm")


x=new_list[count-1]
print(x)

new_list.pop()
print("list without 1")
print(new_list)
y=pepe[count]
print(y)

if opose("[","]") == True:
    new_list.append("great")
else:
    new_list.append("not so great")

print(new_list)
    

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