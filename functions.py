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

# ex challenge 1
def hello_world_printer():
    print("hello world")


hello_world_printer()


# ex challenge 2

def name_printer(par1):
    print(par1)
    

name = input("Please enter your name.")
name_printer(name)

# ex challenge 3 - cal vol
length = int(input("Enter length"));
width = int(input("Enter width"));
height = int(input("Enter height"));

def calculateVolume(length, width, height):
    return length * width * height

volume = str(calculateVolume(length, width, height))
print(volume + " cubic feet.")


# ex challenge 4 - celsius to fahrenheit

celsius_temp = int(input("Enter temperature in celsius"))

def celsius_to_fahrenheit(temp):
    return ((1.8 * temp) + 320)/10  # multiplied and divided by 10 to solve approximation error
    # return (1.8 * temp) + 32

fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print("The Fahrenheit equivalent of " + str(celsius_temp) + ' is ' + str(fahrenheit_temp))

