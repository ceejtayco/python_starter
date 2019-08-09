#List less than 10
a = []
less_than_10 = []
for x in range(10):
    number = int(input('Enter number: Iteration(' + str(x+1) + '): '))
    a.append(number)

print('Original List:', a)

for x in a:
    if a[x] < 10:
        less_than_10.append(a[x])

print('List less than 10:', less_than_10)