#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


def sum_of_multiples(limit):
    multiples = list(range(1, limit+1))
    sum = 0
    new_multiples = []

    for x in multiples:
        if x % 3 == 0 or x % 5 == 0:
            new_multiples.append(x)
            sum+= x
    
    print(new_multiples,'=',sum)
sum_of_multiples(int(input('Enter a number: ')))