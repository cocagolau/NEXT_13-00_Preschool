from Tkinter import *

app = Tk()
app.title("your tkinter application")
app.geometry('450x500+100+100')

my_entry_field = Text(app)
my_entry_field.pack(padx=10, pady=10)

def get_data():
	print(my_entry_field.get("1.0",END))
def insert_data():
	my_entry_field.insert("1.0","Some Text")
def delete_data():
	my_entry_field.delete("1.0",END)

Button(app, text="get_data", command=get_data).pack()
Button(app, text="insert_data", command=insert_data).pack()
Button(app, text="delete_data", command=delete_data).pack()


app.mainloop()