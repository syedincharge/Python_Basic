#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com
import calendar

def find_calendar(month, year):
    """Simple calendar display function"""
    if 1 <= month <= 12:
        print(f"\nCalendar for {calendar.month_name[month]} {year}:")
        print("=" * 35)
        print(calendar.month(year, month))
        print("=" * 35)
    else:
        print("Invalid month! Please enter 1-12")

# Quick usage
if __name__ == "__main__":
    # Example 1: Hardcoded values
    print("Example 1: March 2024")
    find_calendar(3, 2024)
    
    # Example 2: User input
    print("\nExample 2: Your choice")
    try:
        y = int(input("Enter year: "))
        m = int(input("Enter month (1-12): "))
        find_calendar(m, y)
    except:
        print("Please enter valid numbers!")
        
        
