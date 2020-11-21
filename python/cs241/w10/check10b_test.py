"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""

def sort(numbers):
    for f_order in range(1,len(numbers)):
        print(f_order)
        new_biger = f_order
        new_runner = numbers[f_order]
        print("list member - 1",numbers[f_order-1]," and new list member",new_runner)
        while new_biger > 0 and numbers[new_biger-1] > new_runner:
            numbers[f_order] = numbers[f_order-1]
            new_biger = new_biger - 1
            print("new_runner",new_runner)
            print("list memeber",numbers[f_order]) 
        numbers[new_biger]=new_runner
        print("new_biger")
        print(numbers[new_biger])
        print("new_runner")
        print(new_runner)          
numbers = [0,1,2,3,4,9,8,7,6,5]
print(numbers)
def main():
    """
    Tests the sorting process
    """    
    sort(numbers) 

if __name__ == "__main__":
    main()