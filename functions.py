def prints_four():
    print("this")
    print("is")
    print("an")
    print("eg")
    
    
prints_four()
prints_four()
prints_four()
prints_four()


# Eg 2
def function_name():
    print(2 + 2)
    

function_name()

# Eg 3: Passing parameters
def function_name(parameter):
    print(parameter + 2)
    

function_name(8)


# Eg 4: Multiple parameters
first_str = "The number "


def multi_params(p1, p2, p3):
    print(p1 + str(p2) + p3)
    

multi_params(first_str, 5, " is an integer.")

# Eg 5: Default parameters

def default_eg(num1=7, num2=8):
    print(num1 * num2)


default_eg()
default_eg(1)
default_eg(2, 3)

# Eg 6: Return statements in functions

def default_eg(num1=7, num2=8):
    return num1 * num2


data1 = default_eg()
data2 = default_eg(1)
data3 = default_eg(2, 3)

print(data1, data2, data3)