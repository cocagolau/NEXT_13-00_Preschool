def msg_print(value) :
	msg.set(value)

def input_ans() :
	return ans.get()

#-----------------------------

# veriry the number
def veri(com_value) :
	veri_num = 0
	for i in range(3) :
		for j in range(3-i) :
			if com_value[i] == com_value[3-j] :
				veri_num = veri_num + 1
	return veri_num


# arrary the answer
def ans_input () :
	#ans = raw_input("   Please, Guess the number:  ")
	#while len(ans) != 4 :
	#	ans = raw_input("   please, Guess a four-digit number: ")
	ans_arr = [0,0,0,0]
	for i in range(0,4) :
		ans_arr[i] = int(answer[i])
	return ans_arr

#-----------------------------
# randomize the number
from random import randint
com = [0,0,0,0]
while veri(com) > 0 :
		com = [randint(0,9), randint(0,9), randint(0,9), randint(0,9)]


#-----------------------------
# Design compoents
from Tkinter import *
base = Tk()
base.title("Welcome to Baseball World!")
base.geometry('300x600+200+200')

# Variation
msg = StringVar()
msg.set('Please, Guess the number')

answer = ""
if answer != "" :
	ans_input(answer)

# Componets
Button(base, text="New Game").pack()
Label(base, text="Welcom, Baseball Game").pack()

ans = Entry(base)
ans.pack()


click_ans = Button(base, text="Input", command=input_ans)
click_ans.pack()

final = Label(base, textvariable=msg)
final.pack()

base.mainloop()

