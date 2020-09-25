import random
from random import randint
# the counter will let us now how manny tries have been done

print("Welcome to the number guessing game!")

def gueessing_game():
	random_seed= input("Enter random seed: ")
	random.seed(random_seed)
	random_number= randint(1,100)
	
	def guessing_answer():
		count =1
		guess = int(input("\nPlease enter a guess: "))
		while  guess != random_number:
			count += 1
			if guess < random_number:
				print("Higher")
				guess = int(input("\nPlease enter a guess: "))
			else:
				print("Lower")
				guess = int(input("\nPlease enter a guess: "))
		print("Congratulations. You guessed it!\n"
			"It took you", count,"guesses.\n")
		the_end=input("Would you like to play again (yes/no)? ")
		if the_end == ("yes"):			
			guessing_answer()
		elif the_end == ("no"): 
			print ("Thank you. Goodbye.")				
		elif the_end == type(int):
			print ("Hey pal the answer must be yes or no")
			the_end=input("Would you like to play again (yes/no)? ")	 
		else:
			print ("Hey pal the answer must be yes or no")
			the_end=input("Would you like to play again (yes/no)? ")	
	guessing_answer()
gueessing_game()