#Return the common numbers in a list

a = list(range(1,20,2))
b = list(range(1,20,3))
print(a)
print(b)

print(set(a).intersection(b))