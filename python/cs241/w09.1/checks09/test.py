def hi():
   hello = str(input("good morning! how you doing?\n"))
   print("thanks for saying", hello)
   raise ValueError("I don't want emoticons!")  

hi()