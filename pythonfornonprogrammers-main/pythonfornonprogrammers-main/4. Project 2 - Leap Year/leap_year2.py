print("Program to find the leap year \n")

try:
    year = int(input("Enter the Year: "))
    
    # Leap year rules:
    # 1. Divisible by 4 AND not divisible by 100, OR
    # 2. Divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"✅ {year} is a Leap Year")
    else:
        print(f"❌ {year} is Not a Leap Year")
        
except ValueError:
    print("Error: Please enter a valid year!")