from random import randint

fuel = randint(10, 25)
gallon = randint(200, 400)

# mpg = miles/gallon;
mpg = gallon/fuel
print(mpg)
print('miles = ', gallon)
print('gallon = ', fuel)