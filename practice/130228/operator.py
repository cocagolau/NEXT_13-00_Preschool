'''
stock ={	
	'name' : 'Goog',
	'shares' : 100,
	'price' : 490.10
}


print "{0} {1} {2}".format('Goog',100,490.10)
print "{name} {shares} {price}".format(name='Goog',shares=100, price=490.10)
print "Hello {0}, your age is {age}".format("Elwood", age=47)
print "Use {{and}} to output single curly braces".format()

print "{0[name]:8} {0[shares]:8d} {0[price]:8.2f}".format(stock)
#print "{name:8} {shares:8d} {price:8.2f}".format(stock) 

#------ 

name = "Elwood"
print "{0:<10}".format(name)
print "{0:->10}".format(name)
print "{0:^10}".format(name)
print "{0:0^10}".format(name)

x = 42
print "{0:10d}".format(x)
print "{0:10b}".format(x)
print "{0:10x}".format(x)
print "{0:10o}".format(x)
print "\n"
y = 3.1415926
print "{0:10.2f}".format(y)
print "{0:10.2e}".format(y)
print "{0:+10.2f}".format(y)
print "{0:+010.2f}".format(y)
print "{0:10.2%}".format(y)
print "\n"
print "{0:{width}.{precision}f}".format(y, width=10, precision=3)
print "{0:{1}.{2}f}".format(y,10,3)
print "\n"

name1 = "Guido"
print "{0!s:-^20}".format(name1) 


 # dic operator
d = {}
d[1,2,3] = "foo"
d[1.0,3] = "bar"
print d

# set operator
aa = set(["a","b","c",1,2,3])
bb = set(["b","d","f",3,4,5])

print aa,bb
print aa | bb
print aa & bb
print aa - bb
print bb - aa
print aa ^ bb
print bb ^ aa
print len(aa), len(bb)
print max(aa), min(aa)
print max(bb), min(bb)
a1 = 10
b1 = 12
a1 <<= b1
print a1 '''

aaa = 1
bbb = 2
ss = 'sdfasf'
print eval(ss)








