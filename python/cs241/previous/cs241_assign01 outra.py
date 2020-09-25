import random
from random import randint
# the counter will let us now how manny tries have been done in total
count =0
print("Welcome to the number guessing game!")

def gueessing_game():
	randSeed= input("Enter random seed: ")
	random.seed(randSeed)
	randNum= randint(1,100)
	print(randNum)
		
	def new_input():
		guess = int(input("\nPlease enter a guess: "))
		global count
		count += 1
		if guess < randNum:
			print("Higher\n")
			new_input()
		elif guess > randNum:
			print("Lower\n")
			new_input()
		elif guess == randNum:
			print("Congratulations. You guessed it!\n"
			"It took you", count,"guesses.\n")
			def asking_new_try():
				will_try=input("Would you like to play again (yes/no)? ") 
				if will_try == ("yes"):					
					gueessing_game()			
				elif will_try == ("no"): 
					print ("Thank you. Goodbye.")				
				else:
					print ("Hey pal the answer must be yes or no")
					asking_new_try()
			asking_new_try()
	new_input()
gueessing_game()
