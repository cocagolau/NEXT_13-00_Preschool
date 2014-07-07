import time


def no_2(num) :
	for i in range(num) :
		for j in range(num) :
			if i <= j :
				print ("*"),
			else :
				print (" "),
		print("")
def no_3(num) :
	for j in range(num) :
		for i in range(num) :
			if num - j - 1 > i :
				print " ",
			else :
				print "*",
		print("")
def no_4(num) :
	for j in range(num) :
		for i in range(num) :
			if num - j > i :
				print "*",
			else :
				print " ",
		print("")
def no_5(num) :
	mid_num = int(num/2)
	if num%2 == 0 :
		mid_num = mid_num - 1

	for i in range(mid_num+1) :
		for j in range(num) :
			if j <= mid_num :
				#if mid_num-i > j :
				if j >= mid_num-i :
					print "*",
				else :
					print " ",
			else :
				if num%2 == 0 :
					if j-mid_num-1 <= i :
						print "*",
					else :
						print " ",
				else :
					if j-mid_num-1 < i :
						print "*",
					else :
						print " ",
		print("")
def no_6(num) :
	mid_num = int(num/2)
	if num%2 == 0 :
		mid_num = mid_num - 1

	for i in range(mid_num+1) :
		for j in range(num) :
			if j <= mid_num :
				if j-i >= 0 :
					print "*",
				else :
					print " ",
			else :
				if (num-1-j)-i >= 0 :
					print "*",
				else :
					print " ",
		print("")
def no_7(num) :
	mid_num = int(num/2)
	if num%2 == 0 :
		mid_num = mid_num - 1

	for i in range(num) :
		for j in range(num) :
			if i <= mid_num :
				if j <= mid_num :
					if j-i >= 0 :
						print "*",
					else :
						print " ",
				else :
					if (num-1-j)-i >= 0 :
						print "*",
					else :
						print " ",
			else :
				if j <= mid_num :
					if j-(num-1-i) >= 0 :
						print "*",
					else :
						print " ",
				else :
					if (num-1-j)-(num-1-i) >= 0 :
						print "*",
					else :
						print " ",
		print("")
		if i >= mid_num :
			time.sleep(1)


num = 5
num1 = 11
num2 = 10
'''no_1(num)
print("")
no_2(num)
print("")
no_3(num)
print("")
no_4(num)
print("")
no_5(num)
print("")
no_6(num)
print("")'''

no_7(num1)
print("")
#no_7(num2)
#print("")
