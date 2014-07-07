'''
def countdown(n):
	print "countdown"
	while n >= 0:
		yield n
		n -= 1

for i in countdown(5):
	print i, '''
#----------

import time
def tail(f):
	f.seek(0,2)
	while True:
		line = f.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

