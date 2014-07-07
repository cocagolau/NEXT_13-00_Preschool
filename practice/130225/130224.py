def pan_print(pan_data) :
	for i in range(9) :
		print pan_data[i],
		if i%3 == 2 :
			print ""	


num_pan = []
num_space = " "
num_in = 0

for i in range(1,9) :
	num_pan.append(i)
num_pan.append(num_space)
pan_print(num_pan)

while num_in != 9 :
	num_in_position = 0
	num_0_position = 0

	num_in = input("Input number: ")


	for i in range(9) :
		if num_pan[i] == num_in :
			num_in_position = i
		elif num_pan[i] == num_space :
			num_0_position = i
	print ("input : %d    space : %d" %(num_in_position, num_0_position))

	

	num_pan[num_0_position] = num_pan[num_in_position]
	num_pan[num_in_position] = num_space

	pan_print(num_pan)
print "break"