com_num = input("How many computers you have : ")
prog = raw_input("How much each runtime of programs : ")
prog_run = prog.split(',')
prog_num = len(prog_run)
program = []
program_sum = 0

for i in range(prog_num) :
	program.append(int(prog_run[i]))

program.sort()
'''
for com in range(com_num):
	if com == 0:
		print "computer: %d" %com_num,
		print program

	else :
		for pro in range(prog_num) :
			program_totaltime += program[pro]
			if com >= pro :
				print "computer %d : %d" %(pro+1, program[pro])			'''



if com_num == 1:
	print "computer: %d" %com_num,
	print program

elif com_num >= prog_num :
	for i in range(prog_num) :
		print "computer %d : %d" %(i+1, program[i])

else :
	for com in range(com_num):
		for pro in range(prog_num) :
			program
			if sum(program) 




'''
for com in range(com_num) :
	for pro in range(prog_num) :'''
		




