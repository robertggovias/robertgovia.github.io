counting=0
countings=0
counts=0
theFile = input("Enter file: ")
text = open(theFile,"r")

'''for lines in text:
    counting += 1
    words=lines.split()
    for lines in words:
        countings +=1
print("The file contains {} lines and {} words.".format(counting,countings))'''
'''for pline in text:
    worthy=pline.split()
    print("super ya aprendí {} que {} puedo {} usar {} en una {} lista".format(worthy[1],worthy[2],worthy[3],worthy[4],worthy[5]))'''
for pline in text:
    worthy=pline.split()
    for create in worthy:
        print(create)

    print("super ya aprendí {} que {} puedo {} usar {} en una {} lista".format(worthy[1],worthy[2],worthy[3],worthy[4],worthy[5]))

    
text.close()