stock = {
"name"   : "GOOG",
"shares" : 100,
"price"  : 490.10
}

prices = {
	"GOOG" : 123,
	"AAPL" :234,
	"IMB"  : 24,
	"MSFT" : 234
}

name = stock["name"]
value = stock["shares"] * stock["price"]

print stock
print name, value

if "IMB" in prices:
	p = prices["IMB"]
else:
	p =0.0

s = prices.get("IMB",0.0)
print p,s
print prices
syms = list(prices)
print syms

del prices["IMB"]
print prices

