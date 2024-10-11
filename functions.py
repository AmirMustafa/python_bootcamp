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