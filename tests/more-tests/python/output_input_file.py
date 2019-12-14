my_list = [i ** 4 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")
f = open("output.txt","r")
print f.read()
f.close

with open("text.txt", "w") as textfile:
  textfile.write("Success!")
  
with open("text.txt", "r") as textfile:
  print textfile.read(5)
  
with open("again.txt","w") as my_file:
  my_file.write("this is great")



