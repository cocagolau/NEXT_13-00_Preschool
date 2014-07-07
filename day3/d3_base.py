# randomize the number
from random import randint
com = [0,0,0,0]

# veriry the number
	veri = 0
	while veri == 0 :
		#veri_arr = [0,0,0,0,0,0,0]
		veri_num = 0
		for i in range(3) :
			for j in range(3-i) :
				if com[i] == com[3-j] :
					#veri_arr[veri_num] = 1
					veri_num = veri_num + 1
		#print veri_arr
		if veri_num > 0 :
			com = [randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
			veri = 0
		else :
			veri = 1


# The Main Screen of game
print("------------------------------")
print com
print("   Welcome, Baseball Game")


# input user's number
ans = 0
while ans != com :
	# array number
	print("------------------------------")
	ans = raw_input("   Please, Guess the number:  ")
	ans_arr = [0,0,0,0]

	while len(ans) != 4 :
		ans = raw_input("please, Guess a four-digit number: ")
	
	for i in range(0,4) :
		ans_arr[i] = int(ans[i])
	print("------------------------------")
	print ans_arr


	# evaluate number 
	strike_num = 0
	ball_num = 0
	for i in range(4) :
		for j in range(4) :
			if i == j :
				if com[i] == ans_arr[j] :
					strike_num = strike_num + 1
			else :
				if com[i] == ans_arr[j] :
					ball_num = ball_num + 1


	# print evaluated
	if strike_num + ball_num == 0 :
		print ("Out!")
	else :
		print strike_num, "strike", ball_num, "ball"


# Win
print("------------------------------")
print("   perfect! U WIN!") 

