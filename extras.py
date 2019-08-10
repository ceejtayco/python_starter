# #List
# number = list(range(1,11))

# print('This is a list',number)
# #Same as  above
# number = [x for x in range(1,11)]
# print('New list', number)

# #Print a name
# name = 'John Smith'
# print(name[:-1])

#CODING EXERCISES
#Write a function that returns the maximum of two numbers
x = int(input('Input 1st number: '))
y = int(input('Input 2nd number: '))

hold = ''
if x > y:
    hold = x
else:
    hold = y

print('Maximum number is' , hold)

