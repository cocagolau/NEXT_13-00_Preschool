def msg_print(value) :
	msg.set(value)

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
	temp = ans_input_en.get()

	msg_print ("Please, Guess the number")

	while len(temp) != 4 :
		msg_pring ("Please, Guess a four-digit number")

	ans_arr = [0,0,0,0]
	for i in range(4) :
		ans_arr[i] = int(temp[i])
	print ans_arr


'''
def ans_input () :
	ans = raw_input("   Please, Guess the number:  ")
	while len(ans) != 4 :
		ans = raw_input("   please, Guess a four-digit number: ")
	ans_arr = [0,0,0,0]
	for i in range(4) :
		ans_arr[i] = int(ans[i])
	return ans_arr

def send_ans() :
	temp = ans_input_en.get()
	ans_input(temp)'''


# randomize the number
from random import randint
com = [0,0,0,0]
while veri(com) > 0 :
		com = [randint(0,9), randint(0,9), randint(0,9), randint(0,9)]


from Tkinter import *
base = Tk()
base.title("Welcome to Baseball World!")
base.geometry('300x600+200+200')

msg = StringVar()
msg.set('')

ans_in = StringVar()
ans_in.set('')


Button(base, text="New Game").pack()
Label(base, text="Welcom, Baseball Game").pack()

ans_input_en = Entry(base)
ans_input_en.pack()


ans_input_bu = Button(base, text="Send", command=ans_input)
ans_input_bu.pack()

final = Label(base, textvariable=msg)
final.pack()



# Print The Main Screen of game
print("-----------------------------------------------")
print("     Welcome, Baseball Game:  %d %d %d %d" %(com[0],com[1],com[2],com[3]))
print("-----------------------------------------------")


while 1 :
	ans = ans_arr
	while veri(ans) > 0 :
		msg_print("Error: Please, avoid duplication of The answer")
		ans = ans_input()

	#print evaluated result
	eval_final = evalu(com, ans)
	if com != ans :
		if eval_final[0] + eval_final[1] == 0 :
			msg_print("Out!")
		else :
			msg_print("%d strike, %d ball" %(eval_final[0], eval_final[1]))
	else :
		msg_print("perfect! U WIN!") 
		break

base.mainloop()






