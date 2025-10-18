
print("========   Using Function for reusability  ===========\n")

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print("========   Checking number is Even  Or  Odd   ========\n")

number = int(input("Please enter the number :  \n"))
result = check_even_odd(number)
print(f"{number} is {result}")