from random import randint
answer = randint(0,9)
guess = 0

while guess != answer:

	guess = input("Guess the Number")

	if guess == answer:
		print("U win!")
	else:
		if guess > answer:
			print ("Too Much")
		else:
			print ("Too Lose")

print("gg")