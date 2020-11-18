def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     print(alist)

alist = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
insertionSort(alist)
print(alist)