'''
def abc(x,y):
	return x+y

print abc(10,20)

b = (lambda x,y: x+y)(10,20)
print b

print range(5)

c = list(map(lambda x:x**2, range(5)))
print c


#--------
from functools import reduce
d = reduce (lambda x,y: y+x, 'abcde')
print d
print "\n"

e = list(filter(lambda x : x<5, range(10)))
print e

f = list(filter(lambda x : x%2 == 1, range(10)))
print f 

#-------
from pylab import *
x = linspace (-1.6, 1.6, 10000)
f = lambda x : (sqrt(cos(x)) * cos(200*x) + sqrt(abs(x))-0.7) *pow((4-x*x),0.01)

plot(x, map(f,x))
show() 

# self
def countdown(n):
	if  n == 0:
		print "stop"
	else :
		print n
		countdown(n-1)

countdown(5) '''

char = []
abc = "be happy"

for i in abc:
	char.append(i)

print char







