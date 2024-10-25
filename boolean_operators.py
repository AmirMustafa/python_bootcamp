print(4 > 1 and "word" == "word") # True and True
print(0 > 1 and "word" == "word") # False and True
print(4 > 1 and "word" == "word2") # True and False


print(4 > 1 or "word" == "word") # True and True
print(0 > 1 or "word" == "word") # False and True
print(4 > 1 or "word" == "word2") # True and False
print(0 > 1 or "word" == "word2") # False and False

print(not 5000 > 0) # not True
print(not "Python" != "Python") # not False