def hi():
   hello = str(input("good morning! how you doing?\n"))
   print("thanks for saying", hello)
   raise ValueError("Please use words, I dont understand emoticons!")
try:
    hi()
except ValueError as e:
    print("Got a value error: ", e)