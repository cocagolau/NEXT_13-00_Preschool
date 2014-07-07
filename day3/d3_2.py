result_f = open("result.txt")
first = 0
second = 0


for score in result_f :
	score = float(score)
	if first <= score :
		first = score

print first
print second

result_f.close()