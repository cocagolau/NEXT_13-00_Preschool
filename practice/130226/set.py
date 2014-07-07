s = set([1,1,2,3,4])
t = set("Hello")

print s
print t

a = t | s
b = t & s
c = t - s
d = t ^ s

print a
print b
print c
print d

d.add(6)
d.update([6,7,8])
d.remove(8)

print d