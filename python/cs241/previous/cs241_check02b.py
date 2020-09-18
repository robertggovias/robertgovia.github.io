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