import random
number = random.randint(1, 25)
guessesTaken = 0

print ("I am thinkg of a number between 1 & 25...")

while guessesTaken < 5:
	guess = int(raw_input("Take a guess:"))
	guessesTaken +-1
	guessesTaken = guessesTaken + 1

	
	if guess < number:
   		print "Try something higher..."
	
	elif guess > number:
    		print "Try something lower..."
	
	elif guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print ("Good job, you guessed it in: " + guessesTaken + " guesses!")

if guess != number:
	number = str(number)
	print ("Too slow! The number was " + number)

