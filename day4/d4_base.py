
# veriry the number
def veri(com_value) :
	veri_num = 0
	for i in range(3) :
		for j in range(3-i) :
			if com_value[i] == com_value[3-j] :
				veri_num = veri_num + 1
	return veri_num
# evaluate the number
def evalu(com_value, ans_value) :
	stri_num = 0
	ball_num = 0
	for i in range(4) :
		for j in range(4) :
			if com_value[i] == ans_value[j] :
				if i == j :
					stri_num = stri_num + 1
				else :
					ball_num = ball_num + 1
	return stri_num, ball_num
#input the answer
def ans_input () :
	ans = raw_input("   Please, Guess the number:  ")
	while len(ans) != 4 :
		ans = raw_input("   please, Guess a four-digit number: ")
	ans_arr = [0,0,0,0]
	for i in range(0,4) :
		ans_arr[i] = int(ans[i])
	return ans_arr

# randomize the number
from random import randint
com = [0,0,0,0]
while veri(com) > 0 :
		com = [randint(0,9), randint(0,9), randint(0,9), randint(0,9)]

# Print The Main Screen of game
print("-----------------------------------------------")
print("     Welcome, Baseball Game:  %d %d %d %d" %(com[0],com[1],com[2],com[3]))
print("-----------------------------------------------")

while 1 :
	ans = ans_input()
	while veri(ans) > 0 :
		print("Error: Please, avoid duplication of The answer")
		print("-----------------------------------------------")
		ans = ans_input()

	#print evaluated result
	eval_final = evalu(com, ans)
	if com != ans :
		if eval_final[0] + eval_final[1] == 0 :
			print("\tOut!")
			print("-----------------------------------------------")
		else :
			print("\t\t     Result: %d strike, %d ball" %(eval_final[0], eval_final[1]))
			print("-----------------------------------------------")
	else :
		print("\tperfect! U WIN!") 
		print("-----------------------------------------------")
		break