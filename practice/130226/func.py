def divide(a,b,c=10):
	q = a // b
	r = a- q*b
	return (q,r,c)
quo, rema, ha = divide(1456,33)

count = 0
def foo() :
	global count
	count += 1
foo()
print count

print quo,rema,ha





