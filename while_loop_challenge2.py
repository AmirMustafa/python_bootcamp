positive_int = int(input('Enter a positive integer: '))
sum_number = 0

while positive_int > 0:
    print(positive_int)
    sum_number += positive_int
    positive_int -= 1

print(sum_number)
