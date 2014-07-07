
from Tkinter import *

def save_data():
	file_d = open('deliveries.txt','w')
	file_d.write("Depot: ")
	file_d.write("%s\n" %depot.get())

	file_d.write("Descripttion: ")
	file_d.write("%s\n" %desc.get())

	file_d.write("address: ")
	file_d.write("%s\n" %addr.get("1.0",END))
	file_d.close()

	#depot.delete(0,END)
	depot.set(None)
	desc.delete(0,END)
	addr.delete("1.0",END)

app=Tk()
app.title("Next deliveries")
app.geometry('600x600+100+100')

Label(app, text="Depot").pack()

depot = StringVar()
depot.set(None)

depots=["loc.1","loc.2","loc.3","loc.4"]
OptionMenu(app, depot, *depots).pack()

'''
OptionMenu(app, depot, "loc.1","loc.2","loc.3").pack()
Radiobutton(app, text="loc.1", value="loc.1", variable=depot).pack()
Radiobutton(app, text="loc.2", value="loc.2", variable=depot).pack()
Radiobutton(app, text="loc.3", value="loc.3", variable=depot).pack()

depot = Entry(app)
depot.pack()'''

Label(app, text="desc").pack()
desc = Entry(app)
desc.pack()

Label(app, text="address").pack()
addr = Text(app)
addr.pack()

Button(app, text="Save", command=save_data).pack()
app.mainloop()
