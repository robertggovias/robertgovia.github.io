import sys
file_name = "integers.txt"
text = []
try:
    fh = open(file_name,'r')    
except IOError:
    print("cannot open", file_name)
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[1])