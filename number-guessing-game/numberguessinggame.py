from random import randint # randint function is used to generate random integer

print("""
Welcome to the Number Guessing Game!
I'm thinking of number between 1 and 100.
Try to guess the correct number!

Please select the difficulty level:""")

difficulties = {
	1: ("Easy", 10),
	2: ("Medium", 5),
	3: ("Hard", 3),
}

for difficulty_id in difficulties:
	print(f"{difficulty_id}. {difficulties[difficulty_id][0]} " + \
		f"({difficulties[difficulty_id][1]} chances)")

difficulty_id = None
while not difficulty_id in difficulties: # user input validation loop
	try:
		difficulty_id = int(input("\nEnter your choice: "))
	except ValueError: # if user input is empty or non-integer
		difficulty_id = None
chosen_difficulty = difficulties[difficulty_id]

print(f"\nGreat! You have selected the {chosen_difficulty[0]} difficulty level")
print("Let's start the game!")

number_to_guess = randint(1, 100)
chances = chosen_difficulty[1]

while True:
	try: # user input validation loop
		guess = int(input("\nEnter your guess: "))
	except ValueError: # if user input is empty or non-integer
		continue

	chances -= 1

	if number_to_guess == guess:
		exit(f"Congratulations! You guessed the correct number in {chosen_difficulty[1] - chances} attempts.\n")
	elif number_to_guess > guess:
		print(f"Incorrect! The number is greater than {guess}")
	else:
		print(f"Incorrect! The number is less than {guess}")

	if chances <= 0:
		exit("You're out of attempts!\n")
