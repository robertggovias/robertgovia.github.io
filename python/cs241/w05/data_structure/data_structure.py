import os

os.getcwd()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Gets the folder to the current file
my_file = os.path.join(THIS_FOLDER, 'file.txt') # Generates the absolute path to the file
os.chdir(THIS_FOLDER)
"""
This file contains psuedocode developed by together by the class one semester...
"""
#os.listdir()
# Open the file
lr = open("stacks04.txt","r")
lines = lr.readlines()
'''count=0
for i in lines:
    print("line {}: {}".format(count, line.strip())
'''
# Python code to 
# demonstrate readlines() 
'''  
L = ["Geeks\n", "for\n", "Geeks\n"] 
  
# writing to file 
file1 = open('myfile.txt', 'w') 
file1.writelines(L) 
file1.close() 
  
# Using readlines() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip())) 
'''
# Read through it character by character

# One way to do this for this program, is to read line by line
# and then call line.strip() to get rid of any whitespace
#open(text_file)
#for (line in ...)
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

# If there is anything on the stack, the braces didn't match