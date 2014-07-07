
import urllib2
import time

def get_price():
	page = urllib2.urlopen("http://beans.itcarlow.ie/prices.html")
	text = page.read().decode("utf8")
	where = text.find(">$")
	start_of_price = where + 2
	end_of_price = start_of_price + 4
	return float(text[start_of_price:end_of_price])

price_now = raw_input("Do you want to see the price now (y/n)? ")
if price_now == "y" :
	price = get_price()
	print(price)o

else:
	price = 99.99
	while price > 5.02:
		time.sleep(1)
		price = get_price()
		#print(price)
	print("Buy!")