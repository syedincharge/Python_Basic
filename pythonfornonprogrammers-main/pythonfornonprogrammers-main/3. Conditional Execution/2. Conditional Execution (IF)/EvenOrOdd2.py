print("========   Checking number is Even  Or  Odd   ========")

try:
    number = int(input("Please enter the number :  \n"))
    
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")
        
except ValueError:
    print("Error: Please enter a valid integer!")