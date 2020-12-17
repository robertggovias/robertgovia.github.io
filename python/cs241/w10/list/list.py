fish = ['barracuda','cod','devil ray','eel']
fish.append('flounder')
print("append: ", fish)

fish.insert(0,"anchovi")
print("inserted achovi: ", fish)

more_fish = ['goby','herring','ide','kissing gourami']

fish.extend(more_fish)
print("extended a new list: ", fish)

fish.remove('kissing gourami')
print("removed kissing gourami: ",fish)

print(fish.pop(3))
print("pop index 3 (devil ray): ", fish)

print("take the index of an item of the list (herring): ",fish.index('herring'))

copy_of_fish = fish.copy()
print("copy of the list: ",copy_of_fish)

fish.reverse()
print("The list ordered backward: ",fish)
fish.append("cod")
how_many = fish.count("cod")
print("The amount of times that 'cod' appear on the list: ",how_many)

fish_ages = [1,2,4,3,2,1,1,2]
print("How many times a fish with age one we have: ",fish_ages.count(1))

fish_ages.sort()
print("Ordered list of fish's ages: ",fish_ages)

fish.clear()
print("There is no thing on the list: {}\nDid you see?".format(fish))

print("More about lists, the second part:\n---------------------------------------------------------------------------------------------\n Accessing Characters by Positive Index Number")

ss = "Sammy Shark!"
th5 = ss[4]
print("The fifth letter of frase 'Sammy Shark': {}".format(th5))

print("\nAccessing Characters by Negative Index Number")
th_4 = ss[-4]
print("The fourth last letter of frase 'Sammy Shark': {}".format(th_4))

print("\nSlicing Strings")
sliced = ss[6:11] 
print("Elements from the 7th to 11th, this is sliced: ", sliced)
sliced_first = ss[:5]
sliced_last = ss[7:]

print("Taking everything from the end, {}\n and everything from the begining {}".format(sliced_first,sliced_last))
print("\nAlso with negative numbers")
sliced_negative = ss[-4:-1]

print("Also with negative numbers", sliced_negative)

print("\nSpecifying Stride while Slicing Strings")

each_second = ss[:11:2]
print("Now, each pair indexed letter: ", each_second)
inversed = ss[::-1]
print("An interesting way to print backward with each negative number (in that order)",inversed)


how_many_items = len(ss)
