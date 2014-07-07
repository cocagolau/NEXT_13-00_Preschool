'''
s = ['a','c','b','a']
b = [1,2,3,4,5,6,7,0]
c = "Hello"

s.sort()
print s


a = "Your name is {0} and your age is {age}"
a.format("mike", age=40)
print a '''

a = "Asdf12"
b = "1234"
c = "asdf"
s = "Hellowo rld"
d = "a   a"
bb = ["5","4","3","2","1"]

e = "AAAAABCCCDC"

aa = {
	"A" :1,
	"B" :2,
	"C" :3,
	"D" :4,
	"F" :5
}

ff = {
	"S" :11,
	"T" :12,
	"U" :13
}
aaa = {}
aaa.fromkeys(aa,"0")
print aaa.items()

'''
for i in e:
	print i
print "\n"

print ("\n".join(str(i) for i in e))
	
print e.join('b') '''