a = open("qbdata.txt", "r")
#p=a.readlines()
#print(p)
'''for z in a:
    print(z)'''
'''count=0
for i in a:
    x=i.split()    
    for f in x:
        if f == "14":
            count += 1
crear = "this8is8for8testing8purposes"
palabrasb = crear.split("8")
print(palabrasb)
great=int(input("que palabra quieres, dame un numero: "))
print(palabrasb[great-1])
print(count)        
a.close()'''

counting=0
countings=0
theFile = input("Enter file: ")
text = open(theFile,"r")
for lines in text:
    counting += 1
    words=lines.split()
    for lines in words:
        countings +=1
print("The file contains {} lines and {} words.".format(counting,countings))

