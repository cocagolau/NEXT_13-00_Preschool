scores = {}
result_f = open("result2.txt")
for line in result_f :
	(name, score) = line.split()
	scores[float(score)] = name
result_f.close()

'''for key in scores.keys() :
	print("name: %s ..... score: %1.2f" %(scores[key],key))'''

for each_score in sorted(scores.keys()):
	print(scores[each_score], each_score)
