stock = ('goog',100,400,10)
address = ('www.py.com',80)
person = ('first_name', 'lase_name', 'phone')

'''
name,shares,price  =stock
host, port = address
first_name, last_name, phone = person '''

filename = "out.txt"
portfolio = []
for line in open(filename):
	fields = line.split(",")
	name = fields[0]
	shares = int(fields[1])
	price = float(fields[2])
	stock = (name,shares,price)
	portfolio.append(stock)
print portfolio