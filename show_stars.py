#Write a function called show_stars(rows). If rows is 5, it should print the following:

# *
# **
# ***
# ****
# *****

def show_stars(limit):
    for x in range(1,limit+1):
        print('*' * x)

show_stars(int(input('Enter a limit: ')))