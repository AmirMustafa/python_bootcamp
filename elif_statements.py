user_num = int(input("Please enter an integer."))

if user_num < 0:
    print("The no. entered is less than 0")
elif user_num == 0:
    print("The no. entered is 0")
elif 0 < user_num <= 100:
     print("The no. entered is any no. from 1 to 100")
else:
    print("The no. entered is greater than 100")