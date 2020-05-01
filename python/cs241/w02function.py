import random
import math

def favorite_ice_creams():
    ''' This function asks the user for their favorite ice cream flavor.
        It then makes a random comment based on their selection.
        This function takes no parameters and returns nothing '''
    flavor = input("Please enter the name of your favorite ice cream: ")

    responses = ['Everyone loves {}.', 
            '{} is gross!', 
            'You know, Sinatra was fond of {}.',
            'I saw a biopic on the inventor of {}.',
            'Did you know that they don\'t have {} on Neptune?',
            '{} was the name of the band I started in {}.',
            'Did you knonw that {} is made by a secret lab deep in the Himalayas?']
    print(responses[random.randrange(len(responses))].format(flavor))
    return flavor# This is optional if we don't return anything.  Default is None

def print_negativity(x):
    ''' This function checks a value to see if it is non-negative.  If it is,
        it will say so.  This takes an input value and provides no output. 
        Input must be able to be compared to zero. '''
    if x < 0:
        print('{} is negative'.format(x))
    else:
        print('{} is non-negative.'.format(x))

def cowspeak_with_defaults(count = 5, speech = "moo"):
    print("The cow says", end=' ')
    for i in range(count-1):
        print(speech, end=' ')
    else:
        print(speech, end='!\n');

def favorite_number_with_return():
    ''' This function asks a user for their favorite positive number.
        It will keep asking until a positive number is provided and returns
        that number.
        If the value isn't a number, there will be a TypeError '''
    favorite_number = float(input("Please enter your favorite positive number: "))

    while favorite_number <= 0:
        print("That number isn't positive.")
        favorite_number = float(input("Please enter your favorite positive number: "))
   
    return favorite_number


def common_unary_math_return_multiple():
    ''' This function prompts the user for a number, and will the calculate
        some commmon math values for that number.  All of these values
        are returned showing how to return multiple values '''
    try:
        x = favorite_number_with_return()
        print("I received the number {}.".format(x))
    except TypeError:
        print("Did you type something that wasn't a number?  You rebel!")
        return # None
    except ValueError:
        print("Did you give a bad value?")

    return math.fabs(x), math.sin(math.radians(x)), math.cos(math.radians(x)), x**2, x**3, math.exp(x), math.log(x, 2)

def main(test_list = ['favorite_ice_creams', 
        'print_negativity',
        'cowspeak_with_defaults', 
        'favorite_number_with_return',
        'common_unary_math_return_multiple']):
    ''' This function takes a list of functions to test and, based on that list
        will run different tests.  This is used to allow focusing on one
        particular function at a time for demonstration purposes. '''

    if  'favorite_ice_creams' in test_list:
        print("<<<<<<<<<<<<<<<<< Testing favorite_ice_creams() >>>>>>>>>>>>>>>>>")
        result = favorite_ice_creams()
        try:
            print(flavor) # This will fail.  It is not in scope anymore
            print("The value returned was:", result)
        except NameError as e:
            print("I tried to print flavor, but it is not in scope, so it gave a NameError")
            #raise e
            

    if 'print_negativity' in test_list:
        print("\n<<<<<<<<<<<<<<<<< Testing print_negativity() >>>>>>>>>>>>>>>>>")
        try:
            print_negativity(5)
            print_negativity(-5)
            print_negativity('cow')
        except TypeError:
            print("When printing negativity, there was a TypeError.  Did you send it a string?\nI'll bet you sent a string.")

        try:
            print_negativity()
        except TypeError:
            print("When printing negativity, there was a TypeError.\nMaybe this time it was because you forgot to give an input.")


    
    if 'cowspeak_with_defaults' in test_list:
        print("\n<<<<<<<<<<<<<< Testing cowspeak_with_defaults() >>>>>>>>>>>>>>")
        try:
            cowspeak_with_defaults()
            cowspeak_with_defaults(1)
            cowspeak_with_defaults(count = 1)
            cowspeak_with_defaults(speech = 'cluck')
            cowspeak_with_defaults(speech = 'baa', count = 2)
            cowspeak_with_defaults('baa', 2)
        except TypeError:
            print("Did you mix up the order of your inputs?")

    if 'favorite_number_with_return' in test_list:
        print("\n<<<<<<<<<<<<<< Testing favorite_number_with_return() >>>>>>>>>>>>>>")
        for i in range(3):  # Do this 3 times
            try:
                number = favorite_number_with_return()
                print("I received the number {}.".format(number))
            except ValueError:
                print("Did you type something that wasn't a number?  You rebel!")


    if 'common_unary_math_return_multiple' in test_list:
        print("\n<<<<<<<<<<< Testing common_unary_math_return_multiple() >>>>>>>>>>>")
        try:
            abs_x, sin_x, cos_x, x_squared, x_cubed, exp_x, log2_x = common_unary_math_return_multiple()
        except ValueError as e:
            print("There was a problem somewhere calculating one of the values.")
            raise e # Pass up to interpreter.  Code will stop here
        print('The absolute value of x is:', abs_x)
        print('The sine of x is:', sin_x)
        print('The cosine of x is:', cos_x)
        print('x squared is:', x_squared)
        print('x cubed is', x_cubed)
        print('exp(x) is', exp_x)
        print('log_2(x) is', log2_x)

# Intially, leave off this bit
if __name__ == '__main__':
    #random.seed() # Use time of day (default)
    #main(['favorite_ice_creams',])
    #main(['print_negativity',])
    #main(['cowspeak_with_defaults',])
    #main(['favorite_number_with_return',])
    main(['common_unary_math_return_multiple',])
    pass
