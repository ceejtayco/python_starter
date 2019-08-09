#ODD EVEN NUMBERS

number = int(input('Enter a number : '))
odd_even = ''
if number % 2 == 0:
    odd_even = 'even'
else:
    odd_even = 'odd'

print('Number' , str(number) , 'is an ' + odd_even + ' number.')