#Print out lists of divisor of a certain number

divisors = []
number = int(input('Input a number to divide: '))

listRange = list(range(1,number + 1))

for x in listRange:
    if number % x == 0:
        divisors.append(x)

print(divisors)