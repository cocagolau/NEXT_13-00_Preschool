'''def foo(x, items=None):
	if items is None:
		items=[]
	items.append(x)
	return items

print foo(3)
print foo(1)
print foo(2)


# transfer or return parameter 
a = [1,2,3,4,5]
b = []
def square(items):
	for i,x in enumerate(items):
		items[i] = x*x
	return items
b = square(a)
print a
print b 

# ---- #2
def factor(a):
	d = 2
	while (d <= (a / 2)) :
		if ((a/d)*d == a):
			return ((a/d),d)
		d = d+1
	return (a,1)
x,y = factor(1243)
print x, y

# name space
a = 42
b = 37
def foo():
	global a
	a = 13
	b = 0

foo()
print a, b

# func
def countdown(start):
	n = start
	def display():
		print ('T-shirt %d' %n)
	def decrement(n):
		a = []
		a = n
		n -= 1
	while n > 0:
		display()
		declement()

print countdown(5) 


import foo
def bar():
	x = 13
	def helloworld():
		return "Hello World. x is %d" %x

	print foo.callf(helloworld)
print bar()  

from urllib import urlopen
def page(url):
	def get():
		return urlopen(url).read()
	return get

a = page("http://www.naver.com").get()
print a 

def countdown(n):
	def next():
		nonlocal n
		r = n
		n -= 1
		return r
	return next

next = countdown(10)
while 1:
	v = next()
	if not v: break

# decorator
enable_tracing = True
if enable_tracing:
	debug_log = open("debug.log","w")
def trace(func) :
	if enable_tracing:
		def callf(*args, **kwargs):
			debug_log.write("Calling %s: %s, %s\n" %(func.__name__, args, kwargs))
			r = func(*args, **kwargs)
			debug_log.write("%s returned %s\n" %(func.__name__, r))
			return r
		return callf
	else:
		return func

@trace
def square(x):
	return x*x

def square(x):
	return x*x

square = trace(square)'''

#yield









