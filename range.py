# range with 1 argument
one_input = range(5)

for num in one_input:
    print(num)
    
print(type(one_input))

# range with 2 arguments
two_inputs = range(5, 10)

for num in two_inputs:
    print(num)

print(type(two_inputs))

# range with 3 arguments
three_inputs = range(5, 15, 3)

for num in three_inputs:
    print(num)

print(type(three_inputs))

# decrementing loop
three_inputs = range(15, 1, -3)

for num in three_inputs:
    print(num)

print(type(three_inputs))

    