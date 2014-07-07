import math
import random
import copy

def sear_posi (maxi,sear, arr_value) :
	posi_num = []
	for col in range(maxi) :
		for row in range(maxi) :
			if arr_value[col][row] == sear :
				posi_num.append(col)
				posi_num.append(row)
	posi_num.append(posi_num[0]+posi_num[1])
	return posi_num

def get_randvalue (maxi) :
	temp = maxi**2
	indexvalue = []
	for i in range(1,temp) :
		indexvalue.append(i)
	random.shuffle(indexvalue)
	return indexvalue

def array_value (maxi, shuf_value) :
	pan=[[0 for col in range(maxi)] for row in range(maxi)]	
	for col in range(maxi) :
		for row in range(maxi) :
			pan[col][row] = shuf_value[(maxi*col)+row]
	return pan

def print_array (maxi, arr_value) :
	global fin_space
	for col in range(maxi) :
		for row in range(maxi) :
			if arr_value[col][row] == fin_space :
				print ("%2s" %arr_value[col][row]),
			else :
				print ("%2d" %arr_value[col][row]),
		print ""

def change_num (arr_value, posi_1, posi_2) :
	temp = arr_value[posi_1[0]][posi_1[1]]
	arr_value[posi_1[0]][posi_1[1]] = arr_value[posi_2[0]][posi_2[1]]
	arr_value[posi_2[0]][posi_2[1]] = temp



### input size of pan
input_pan_num = input("Please input X / ex) XbyX :  ")
pan_num = input_pan_num

### shuffle number
fin_space = " "
shuf_num = get_randvalue(pan_num)
shuf_num.append(fin_space)

### array number
shuf_pan = array_value(pan_num, shuf_num)
temp_pan = copy.deepcopy(shuf_pan)

### create original_pan
ori_num = []
for i in range(1,pan_num**2) :
	ori_num.append(i)
ori_num.append(fin_space)
ori_pan = array_value(pan_num, ori_num)

### print the array
print_array(pan_num, temp_pan)

### Game start
while temp_pan != ori_pan :

	### input to change the number
	input_ans = input("Please, Input the answer:  ")

	### search coodinate of number
	posi_space = sear_posi(pan_num, fin_space, temp_pan)
	posi_input = sear_posi(pan_num, input_ans, temp_pan)

	### verify changeable number 
	if abs(posi_space[2] - posi_input[2]) != 1 :
		print "U cant change the number"
	else:
		change_num(temp_pan,posi_space,posi_input)
		print_array(pan_num, temp_pan)
print "U win"



