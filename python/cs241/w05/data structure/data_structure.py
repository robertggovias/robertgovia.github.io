import os
"""
This file contains psuedocode developed by together by the class one semester...
"""
os.listdir()
# Open the file
#lr = open("\\stacks01.txt","r")
#print(lr.read())
os.chdir("C:\Users\Robert\Documents\Robert\Host\GitHub\novo backup\robertgovia.github.io\python\cs241\w05")
'''
# Read through it character by character
# One way to do this for this program, is to read line by line
# and then call line.strip() to get rid of any whitespace
open(text_file)
for (line in ...)
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