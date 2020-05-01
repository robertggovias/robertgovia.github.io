import random
from random import randint

print("Welcome to the number guessing game!")
def super_again():
	randSeed= input("Enter a random seed: ")
	random.seed(randSeed)
	randNum= randint(1,100)
	guess = int(input("Please enter a guess: "))
	if ((guess > 0) and (guess < 100)):
		if guess == randNum:
			print("Congratulations. You guessed it")
			again=input("Would you like to play again (yes/no)?") 
			if again == ("no"):
				print ("Thank you. Goodbye.")
			else:
				super_again()
					
		elif guess < randNum:
			print("Higher")
		elif guess > randNum:
			print("Lower")
	else:
		print("the number must be between 0 and 100")
super_again()



