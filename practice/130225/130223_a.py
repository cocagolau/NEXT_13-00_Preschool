from Tkinter import *

app = Tk()
app.title("Hello")
app.geometry('400x300+200+100')

def bu_click():
	msg.set(msg.get()+1)

msg=IntVar()
msg.set(0)


b1 = Button(app, text="click me", width=10, command=bu_click)
b1.pack(side='right', padx=10, pady=10)

l1 = Label(app, textvariable=msg)
l1.pack()

app.mainloop()