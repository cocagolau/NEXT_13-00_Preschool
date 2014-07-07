result_f = open("result2.txt")
scores = []

for line in result_f :
	(name, score) = line.split()
	scores.append(float(score))

scores.sort()
scores.reverse()
result_f.close()

for score in scores :
	print score

