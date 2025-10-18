

def is_leap_year(year):
    """Check if a year is leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Program to find the leap year \n")

while True:
    try:
        year = int(input("Enter the Year (or 0 to exit): "))
        
        if year == 0:
            print("Goodbye!")
            break
            
        if is_leap_year(year):
            print(f"✅ {year} is a Leap Year")
        else:
            print(f"❌ {year} is Not a Leap Year")
            
        # Show examples
        print(f"\nExamples:")
        print(f"2000: {'Leap' if is_leap_year(2000) else 'Not Leap'} (divisible by 400)")
        print(f"1900: {'Leap' if is_leap_year(1900) else 'Not Leap'} (divisible by 100 but not 400)")
        print(f"2024: {'Leap' if is_leap_year(2024) else 'Not Leap'} (divisible by 4 but not 100)")
        print()
        
    except ValueError:
        print("Error: Please enter a valid year!\n")