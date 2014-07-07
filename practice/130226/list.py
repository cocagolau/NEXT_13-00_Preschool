'''names=["a","b","c","d"]
a= names[2]
names[0] = "f"
names.append("f")

print names

names.insert(2,"ff")
print names

b = names[0:2]
c = names[2:]
print b
print c

names=list()
print names	

a=[1,2,3,[1,2,3,[1,2],2],3]
b = a[3][3][1]
print b '''

import sys
if len(sys.argv) != 2 :
	print ("please supply a filename")
	raise SystemExit(1)
f = open(sys.argv[1])
lines = f.readlines()
f.close()

fvalues = [float(line) for line in lines]

print "The Maxi is ", max(fvalues)
print "The Mini is ", min(fvalues)