'''
f = open("foo.txt")
line = f.readline()
while line:
	print line,
	line = f.readline()
f.close()

#----------
f = open("foo.txt")
print ""

for line1 in f :
	print line1
f.close()
'''

## write
f = open("out.txt","w")
principal = 1000
rate = 0.05
numyears = 6
year = 1

while year <= numyears:
	principal = principal * (1+rate)
	#print >> f, "%3d %0.2f" %(year, principal) ## python ver2
	#print("%3d %0.2f" %(year, principal), file=f) ## cant execute
	f.write("%3d %0.2f\n" %(year, principal))
	year += 1
f.close()