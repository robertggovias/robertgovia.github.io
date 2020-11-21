"""
File: ta10-solution.py
Author: Br. Burton
This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    # Base case: if the list has 1 we're done
    if len(items) <= 1:
        return
    
    # Break the list into halves
    mid = len(items)//2    
    left_half=items[:mid]
    rigth_half=items[mid:]
    
    # Recursively call this function to sort each half
    merge_sort(left_half)
    merge_sort(rigth_half)
    

    # Merge the two sorted parts
    i=0
    j=0
    k=0
      
      # As long as there are more items in each list

    while i < len(left_half) and j < len(rigth_half):
        # Get the smaller item from whichever part its in
        if left_half[i] < rigth_half[j]:
            items[k] = left_half[i]
            i += 1
            k += 1
        else:
            items[k] = rigth_half[j]
            j += 1
            k += 1

    
    # At this point, one or the other size is done

    # Copy any remaining items from part1
    
    while i< len(left_half):
        items[k] = left_half[i]
        i += 1
        k += 1
    # Copy any remaining items from ri    
    while j < len(rigth_half):
        items[k] = rigth_half[j]
        j += 1
        k += 1

        




def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()