print("========   Checking number is Even  Or  Odd   ========")

number = int(input("Please enter the number :  \n"))

if number & 1 == 0:  # Bitwise AND with 1
    print("number is Even")
else:
    print("number is Odd")