#Given an array of strings, return another array containing all of its longest strings.

def longest_string(inputList):
    newList = list()
    longest = len(inputList[0])
    for x in range(len(inputList)-1):
        if longest < len(inputList[x+1]):
            longest = len(inputList[x+1])
    
    for x in inputList:
        if len(x) == longest:
            newList.append(x)
    return newList

print(longest_string(["aba", "ab", "ababa", "ab"]))