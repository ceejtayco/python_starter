#Write a function that prints all the prime numbers between 1 and limit where limit is a parameter.

def prime_numbers(limit):
    prime = list()
    
    for x in range(2,limit+1):
        isPrime = True
        for i in range(2,x):
            if x % i == 0 and x != 2:
                isPrime = False
        if isPrime:
           prime.append(x)
    
    print('Prime numbers:', prime)
prime_numbers(int(input('Enter a number: ')))