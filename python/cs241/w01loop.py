'''def function():
  pass
a =0; b=10'''
'''while a<b:
  print(a, end=' ')
  a+=1
print()'''

name = ''
while name != "stop":
  name = input("Enter name: ")
  if name != 'stop':
    age = input("Enter age: ")
    print("Hello, ", name, "=>", int(age)**2)

'''name = "holallllamigo"
i = 0
while i < len(name) and name[i] != 'g':
  if name[i] == 'l':
    i += 1
    continue
  print(name[i], end='')
  i += 1'''
'''y = 134
  x = y//2
  while x > 1:
    if y % x == 0:
      print(y, 'has factor')
      print(y, 'is prime')'''
      
'''ame ="robert"
for c in ame:
  print(c,end=' ')
else:
  print()
for i in range(5):
  print(i, end= ' ')
else:
  print()
i = 0
for item in shopping_list:
  # do something
  i += 1
for i in range(len(shopping_list)):
  shopping_list[i]'''

'''shopping_list = ['canciones', 'shows', 'alegria','amor']
for i,  item in enumerate(shopping_list):
  print(i+1, '.', item, sep='')'''
  
T = [(1,2), (3,4), (5,6)]
for (a,b) in T:
  print('{}^2 + {} = {}'.format(a, b, a**2 + b))
  
for i in range(10):
  for j in range(10):
    print('({}, {})'.format(i, j), end=' ' )
  print()

