num = int(input("Enter a positive number: "))

def getFactorial(num):
    factorial = 1
    for n in range(num, 0, -1):
        factorial = factorial * n
    
    return factorial


factorial = getFactorial(num)
print(factorial)