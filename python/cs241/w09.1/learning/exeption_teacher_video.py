class NoCatsError(Exception):
    def __init__(self, animal=None):
        if animal == None:
            animal = "Cats"
        super().__init__("{}? We hate loudy {}!".format(animal.capitalize(),animal))

class NomOreAnimasError(Exception):
    def __init__(self):
        super().__init__("Enough animals identified.")

def get_some_animals():
    animal = input('please enter an animalito to acquire (Q to quit): ')
    
    if animal.lower()  == "cat" or animal.lower() == "cats":
        raise NoCatsError(animal)

    if animal.lower() == 'q':
        raise NomOreAnimasError

    response =input("Enter the number of {}: ".format(animal))
    if response.lower() == 'q':
        raise NomOreAnimasError
    
    number = int(response)

    return animal,number

def example_main():
    try:
        my_value = float(input("Please enter a number: "))
        print(1/my_value)
    except ZeroDivisionError:
        print("Don't divide by zero, the universe will explode")
    except ValueError:
        print("Just float numbers")

def main():
    
    animal_dictionary = dict()
    done = False

    while not done:
        try: 
            print (get_some_animals())

        except ValueError:
            print("Invalid entry received.")
        except NoCatsError as e:
            print(e.args[0])
        except NomOreAnimasError:
            break
    #
if __name__ == "__main__":
    main()