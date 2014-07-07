from Tkinter import *

app = Tk()
app.title("your tkinter application")
app.geometry('450x300+400+350')

my_entry_field = Entry(app)
my_entry_field.pack(padx=10, pady=10)

def get_field():
	print(my_entry_field.get())

la = Label(app, text="are u ready?", height=3)
la.pack()

b1 = Button(app, text="Get data", command=get_field)
b1.pack(padx=10, pady=10)


def insert_data():
	my_entry_field.insert(0,"Hello ")

b2 = Button(app, text="insert", command=insert_data)
b2.pack(padx=10, pady=10)


def delete_field():
	my_entry_field.delete(0,END)

b3 = Button(app, text="delete", command=delete_field)
b3.pack(padx=10, pady=10)

'''
message = StringVar()
message.set('???')

lm = Label(app, textvariable = message)
lm.pack()
'''

'''
b1 = Button(app, text="Top", width=10)
b1.pack(side='top')
b2 = Button(app, text="Bottom", width=10)
b2.pack(side='bottom')
b3 = Button(app, text="Left", width=10)
b3.pack(side='left')
b4 = Button(app, text="Right", width=10)
b4.pack(side='right') '''

app.mainloop()