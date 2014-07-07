import copy

a = [1,2,[3,4]]
b = copy.deepcopy(a)
print b is a

b.append(100)
print a
print b
b[2][0] = -100
print a
print b