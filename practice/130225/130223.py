from Tkinter import *

app = Tk()
app.title("hello")
app.geometry('300x100+200+100')

b1 = Button(app, text="correct!", width=10)
b1.pack(side='left', padx=10, pady=10)

b2 = Button(app, text="incorrect", width=10)
b2.pack(side='right', padx=10, pady=10)

app.mainloop()

'''
num_game = 0
num_cor = 0
num_incor = 0

while 1 :
	num_inp = input("Please, Input your number: ")

	if num_inp == 1 :
		num_cor = num_cor + 1
	elif num_inp == 2 :
		num_incor = num_incor + 1
	elif num_inp == 0 :
		print ("Question: %d, Correct: %d, Incorrect: %d" %(num_game, num_cor, num_incor))
		break

	num_game = num_game + 1'''

