course=["Math","English","PE","Science","Art"]
grades=[]
count=0
l = len(course)
while count < l:
  grade = int(input("Enter the grade you received for %s: " %(course[count])))
  if (grade>0) and (grade<101):
    grades.append(grade)
    count+=1
  else:
    print "try it again with a number between 0 and 100"
letters=[]
for i in grades:
  if i >= 93:
    letters.append("A")
  elif i >= 90:
    letters.append("A-")
  elif i >= 87:
    letters.append("B+")
  elif i >= 83:
    letters.append("B")
  elif i >= 80:
    letters.append("B-")
  elif i >= 77:
    letters.append("C+")
  elif i >= 73:
    letters.append("C")
  elif i >= 70:
    letters.append("C-")
  elif i >= 67:
    letters.append("D+")
  elif i >= 63:
    letters.append("D")
  elif i >= 60:
    letters.append("D-")
  else:
    letters.append("F")

print letters
for i in range(l):
  hola = "your %s score is %i, you get a %s" %(course[i], grades[i], letters[i])
  print hola
