#Check word if it is palindrome

word = str(input('Input a word to be checked: '))

check_word = ''
palindrome = False
for x in range(len(word)):
    check_word = word[x] + check_word
    
print('Original word: ' + word + '\nReverse Word: ' + check_word)

if word == check_word:
    palindrome = True

print('Palindrome: ' + str(palindrome))