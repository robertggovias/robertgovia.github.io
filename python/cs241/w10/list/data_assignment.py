numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
print("all",numbers)

numbers.insert(0,5)
print("with 5 at the beginnign",numbers)

numbers.remove(2348)
print("without 2348 ",numbers)

second_list=[1,2,4,5,6]

numbers.extend(second_list)
print("with second list", numbers)
numbers.sort()
print("list sorted: ",numbers)
numbers.sort(reverse=True)
print("list backward: ",numbers)
counted = numbers.count(12)
print("how many times '12' appear: ",counted)

indexing = numbers.index(96)
print("the index of '96': ",indexing)
numbeLen = len(numbers)
numbeLenHalf = numbeLen/2
print(numbeLenHalf)
slicing = numbers[0:int(numbeLenHalf)]
print(slicing)

slicing_back = numbers[int(numbeLenHalf)-1:]
print(slicing_back)

lastItems = numbers[-5:]
print("last_items",lastItems)

