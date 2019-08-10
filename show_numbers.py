# Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# For example, if the limit is 3, it should print:
#     0 EVEN
#     1 ODD
#     2 EVEN
#     3 ODD


def showNumbers(limit):
    for x in range(limit + 1):
        if x == 0:
            print(x ,'ORIGIN')
        elif x % 2 == 0:
            print(x ,'EVEN')
        else:
            print(x ,'ODD')

            
showNumbers(int(input('Input a limit:')))