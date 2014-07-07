print("Welcome")

input_val = input("Guess the Number: ")

if input_val == 5:
	print("Win!")
else:
	print("Lose!")
	if input_val > 5:
		print("Too Much")
	else:
		print("Too Low")
	print("Try set another values")

print("End")