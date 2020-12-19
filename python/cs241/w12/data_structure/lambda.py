def sum(x,y):
    return x + y

print(sum(13,1254))

sumy = lambda x,y : x + y
print(sumy(13,1254))

print("Let's see map working --- function , values on a list to iterate the function")

print("this tempetures are in Celcius:\n 36.5, 37, 37.5, 38, 39")

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
 
def celsius(T):
    return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheit,temperatures))
C = list(map(celsius,list(F)))
print(F)
print(C)
forLambda = (36.5, 37, 37.5, 38, 39)
farenheti_with_lambda = list(map(lambda x: (float(9)/5)*x + 32, forLambda))
print(farenheti_with_lambda)
celsius_with_lambda = list(map(lambda x:(float(5)/9)*(x - 32), farenheti_with_lambda ))
print(celsius_with_lambda)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9] 
sum_multiple_list=list(map(lambda x,y,z: x+y+z, a,b,c))
print(sum_multiple_list)

testing_multiple_operations = list(map(lambda x,y,z: x/y*z+45**1%45,a,b,c))
print(testing_multiple_operations)

#The map function of the previous chapter was used to apply one function to one or more iterables. We will now write a function which applies a bunch of functions, which may be an iterable such as a list or a tuple, for example, to one Python object.

from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(func(x))
     return res

family_of_functions = (sin, cos, tan)
print("sin, cos, tan", map_functions(pi, family_of_functions))

print("fibonacci: 0,1,1,2,3,5,8,13,21,34,55\n")
fibonacci= 0,1,1,2,3,5,8,13,21,34,55
odd_numbers = list(filter(lambda x: x%2, fibonacci))
print ("Odd numbers: ",odd_numbers)

eve_number = list(filter(lambda x: x%2 == 0, fibonacci))
print("even numbers: ",eve_number)

print("Now it's time for reduce function")
print("this is the list: 314,1,423,42,4,234,234,12,41,24,12,234,21,41,2")
import functools
hello = list()
print("sum")
print(functools.reduce(lambda x,y:x+y, [314,1,423,42,4,234,234,12,41,24,12,234,21,41,2]))

print("divide")
print(functools.reduce(lambda x,y:x/y, [314,1,423,42,4,234,234,12,41,24,12,234,21,41,2]))

print("multiplication")
print(functools.reduce(lambda x,y:x*y, [314,1,423,42,4,234,234,12,41,24,12,234,21,41,2]))

from functools import reduce
print("conditions")
print("the bigger form 47,11,42,102,13 comparing in pairs")
f = lambda a,b: a if (a > b) else b

print(reduce(f, [47,11,42,102,13]))
print("Al number from 1 to 100 divided")
print(reduce(lambda x, y: x/y, range(1,101)))

print("If you are into lottery, here are the chances to win a 6 out of 49 drawing")
print(reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7)))

