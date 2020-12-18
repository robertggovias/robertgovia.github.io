print("list comprehensions!")

S = [x**2 for x in range(10)]
print(S)

V = [2**i for i in range(9)]
print(V)

print("for Even numbers!")
even = [x for x in S if x%2 ==0]
pluseven = [x//8 for x in S and V if x%2 ==0]
print(even)
print("using V and S")
print(pluseven)

print("for loops")

numbers = range(90)

new_list = []

for c in numbers:
    if c%2 == 0:
        new_list.append(c**2)

print(new_list)

a_new_list = [z**2 for z in numbers if z%2 == 0]

print(a_new_list)


print("\nIt's time por map functions")

kilometer = [1,2,3,4,5]
feet = map(lambda x: float(2000.423424)*x, kilometer)
print(list(feet))

feet_list = [float(2000.423424)*x for x in kilometer]
print(list(feet_list))


newest_list = [1.3, 4,6,8,10,1.2, 3.4, 6.8]
print("float list",newest_list)

#Map values of 'feet' to integers
newest_list_int = list(map(int, newest_list))
print(list(newest_list_int))

#filter 'feet' to only include uneven numbers
uneven = filter(lambda x: x%2,newest_list_int)
type(uneven)
print("uneven",list(uneven))

newest_list2 = [1.3, 4,6,8,10,1.2, 3.4, 6.8]
print("new float list", newest_list2)
new_list2_int = [int(x) for x in newest_list2]
print(list(new_list2_int))

uneven2 = [x for x in new_list2_int if x%2 != 0]
print(uneven2)

from functools import reduce

print(list(newest_list2))
# Reduce `feet` to `reduced_feet` (sum up everything)
reduced_feet = reduce(lambda x,y: x+y, newest_list2)

# Print `reduced_feet`
print(reduced_feet)

#now with list
sumed = sum(newest_list2)
print(sumed)

# Define `uneven`
uneven = [x/2 for x in newest_list2 if x%2==0]

# Print `uneven`
print(uneven)

# Initialize and empty list `uneven`
uneven = []

# Add values to `uneven`
for x in newest_list2:
    if x % 2 == 0:
        x = x / 2
        uneven.append(x)

# Print `uneven`
print(uneven)

divided = []

for x in range(100):
    if x%2 == 0 :
        if x%6 == 0:
            divided.append(x)
print(divided)

mydivided = [x for x in range(300) if x%2 ==0 if x%6 == 0]
print(mydivided)

conditional = [x**8 if x <= 18 else x*10 for x in range(40)]
print(conditional)


nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print("nested list",nested_list)
none_nested = [y for x in nested_list for y in x]
print("none nested", none_nested)

matrix = nested_list
new_matrix = [[row[i] for row in matrix] for i in range(3)]
print("new_matrix", new_matrix)

transposed = []

for i in range(3):
    transposed_row = []
    for row in matrix:
            transposed_row.append(row[i])
    transposed.append(transposed_row)
print("the same",transposed)

matrix_creator = [[0 for x in range(4)] for y in range(6)]
print("other matrix", matrix_creator)
matrix_creator = [[0 for col in range(4)] for row in range(6)]
print("other matrix", matrix_creator)

for x in range(3):
    nested_other = []
    matrix.append(nested_other)
    for row in range(4):
        nested_other.append(0)

print("same nested",nested_other)

x = 0
matrix =[]

while x < 6:
    nested = []
    y = 0
    matrix.append(nested)
    x = x+1
    while y < 4:
        nested.append(0)
        y= y+1

print("and finally",matrix)

from random import randint

random_matrix = [[randint(1,12) for y in range (3)] for x in range(3)]
print(random_matrix)
xr = randint(1,12)
random_matrix = [[xr for y in range (3)] for x in range(3)]
print(random_matrix)

