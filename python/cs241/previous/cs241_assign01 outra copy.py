import random
from random import randint
# the counter will let us now how manny tries have been done
count =0
print("Welcome to the number guessing game!")

def gueessingGame():
	randSeed= input("Enter random seed: ")
	random.seed(randSeed)
	randNum= randint(1,100)
		
	def again():
		guess = int(input("\nPlease enter a guess: "))
		global count
		count += 1
		if guess < randNum:
			print("Higher\n")
			again()
		elif guess > randNum:
			print("Lower\n")
			again()
		elif guess == randNum:
			print("Congratulations. You guessed it!\n"
			"It took you", count,"guesses.\n")
			def goodBye():
				theEnd=input("Would you like to play again (yes/no)? ") 
				if theEnd == ("yes"):					
					again()			
				elif theEnd == ("no"): 
					print ("Thank you. Goodbye.")
				elif 				
				else:
					print ("Hey pal the answer must be yes or no")
					goodBye()
			goodBye()
	again()
gueessingGame()



