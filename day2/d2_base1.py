# randomize the number
from random import randint
com = [0,0,0,0]
veri_sum = 0

# veriry the number
while veri_sum == 0 :
#	veri = [0,0,0,0,0,0,0]
	veri_num = 0
	i = 0

	while i <= 2 :
		j = 3
		while j > i :
			if com[i] == com[j] :
#				veri[veri_num] = 1
				veri_num = veri_num + 1
			j = j - 1
		i = i + 1

#	print veri
	
	if veri_num > 0 :
		com = [randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
		veri_sum = 0
	else :
		veri_sum = 1

# The Main Screen of game
print("------------------------")
# print com
print(" Welcome, Baseball Game")

# input user's number
answer = 0
while answer != com :

	# array inputing number
	print("------------------------")
	answer = input("Please, Guess the number:  ")

	answer0 = answer / 1000
	answer1 = (answer % 1000) / 100
	answer2 = (answer % 100) / 10
	answer3 = answer % 10
	answer = [answer0, answer1, answer2, answer3]

	print "wrong number"
	print answer

	# evaluate inputing number 
	strike_num = 0
	ball_num = 0
	i=0

	while i <= 3 :
		j = 0
		while j <= 3 :
			if i == j :
				if com[i] == answer[j] :
					strike_num = strike_num + 1
			else :
				if com[i] == answer[j] :
					ball_num = ball_num + 1

			j = j + 1
		i = i + 1 

	# print evaluated
	if strike_num + ball_num == 0 :
		print ("Out!")
	else :
		if strike_num != 4 :
			print strike_num, "strike", ball_num, "ball"

print("------------------------")
print("perfect! U WIN!") 