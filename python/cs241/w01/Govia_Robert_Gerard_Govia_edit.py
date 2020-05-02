import random
from random import randint

print("Welcome to the number guessing game!")
def super_again():
	randSeed= input("Enter random seed: ")
	random.seed(randSeed)
	randNum = randint(1,100)
	count=0
	guess = -1

	while randNum != guess:
		print()

		guess = int(input("Please enter a guess: "))
		#print(guess)
		if ((guess > 0) and (guess < 100)):
			count += 1
			if guess == randNum:
				print("Congratulations. You guessed it!")
				print("It took you", count, "guesses.\n")
				again=input("Would you like to play again (yes/no)? ") 
				if again == ("yes"):
					#guess = int(input("Please enter a guess: "))		
					randNum = randint(1,100)
					count = 0
				else:
					print ("Thank you. Goodbye.")
				
			elif guess < randNum:
				print("Higher")
			elif guess > randNum:
				print("Lower")
		else:
			print("the number must be between 0 and 100")
super_again()
