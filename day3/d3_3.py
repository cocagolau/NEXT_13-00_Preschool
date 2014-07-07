result_f = open("result2.txt")
first = 0
second = 0
exc_line = 0


for line in result_f :
	(name, score) = line.split()
	if first < score :
		first = score
		if exc_line == 0 :
			second = first
			exc_line = exc_line + 1

	else:
		if second < score :
			second = score

print first
print second

result_f.close()