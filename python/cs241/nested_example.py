def outside_function():
    ''' This function wraps another function '''
    def inside_function():
        ''' This function is defined inside to demonstrate a point '''
        print("I'm in your inside function!")
    print("I'm in your outside function!")
    inside_function() # Now inside_function is defined, but only inside the scope of this function

def recursive_prompt(depth = 0):
    ''' This function prompts the user for their favorite positive number.
        On failure, it will go down to the next layer.  See how it unwraps.
        Something like this is better served as a loop. '''
    print("Entering level", depth)
    value = input("Please enter your favorite positive number: ")
    try:
        value = int(value)
    except ValueError:
        value = recursive_prompt(depth+1)
    if value <= 0:
        recursive_prompt(depth+1)

    print("The value I currently have at depth {} is {}".format(depth, value))
    print("Leaving level", depth)
    return value


def main():
    '''try:
        inside_function()  # The interpreter doesn't know what you are talking about
    except NameError:
        print("The interpreter didn't know what inside_function() is. Not in scope.")
    outside_function() # This will run the code inside the outside function and thus define the inside_function, but only while running outside_function
    try:
        inside_function()  # The interpreter doesn't know what you are talking about
    except NameError:
        print("The interpreter didn't know what inside_function() is. Not in scope.")
    '''

    print("The value I received was", recursive_prompt())

if __name__ == "__main__":
    main()