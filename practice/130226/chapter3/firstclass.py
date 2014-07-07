'''items = {
	'number': 42,
	'text'  : 'hello world'
}

items["func"] = abs
print items["number"]

import math
items["mod"] = math
items["error"] = ValueError
nums = [1,2,3,4]

items["append"] = nums.append

print items["func"](-45)
print items["mod"].sqrt(4)
print math.sqrt(4)
items["append"](100)

print nums '''

line = "GOOG,100,490,10"
print line
field_types = [str, int, float]
raw_fields = line.split(',')
print raw_fields
fields = [ty  (val) for ty,val in zip(field_types, raw_fields)]
print fields