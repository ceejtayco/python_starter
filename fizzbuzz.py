# Write a function called fizz_buzz that takes a number.

#     If the number is divisible by 3, it should return “Fizz”.
#     If it is divisible by 5, it should return “Buzz”.
#     If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#     Otherwise, it should return the same number.

def fizz_buzz(num1):
    display = ''
    if num1 % 3 == 0 and num1 % 5 == 0:
        display = 'Fizz Buzz'
    elif num1 % 3 == 0:
        display = 'Fizz'
    elif num1 % 5 == 0:
        display = 'Buzz'
    else:
        display = num1
    print(display)

number = int(input('Enter a number: '))
fizz_buzz(number)