"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""

def sort(numbers):
    for f_order in range(1,len(numbers)):        
        temp = numbers[f_order]        
        new_bigger = f_order
        while new_bigger > 0 and numbers[new_bigger - 1] > temp:
            numbers[new_bigger] = numbers[new_bigger-1]
            new_bigger = new_bigger - 1
        numbers[new_bigger] = temp

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """
    numbers = []    
    
    
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()