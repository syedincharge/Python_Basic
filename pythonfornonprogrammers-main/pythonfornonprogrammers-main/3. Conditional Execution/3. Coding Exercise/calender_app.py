import calendar

def find_calendar(month, year):
    """
    Display calendar for a specific month and year
    
    Args:
        month (int): Month number (1-12)
        year (int): Year (e.g., 2024)
    """
    try:
        # Validate month input
        if month < 1 or month > 12:
            print("Error: Month must be between 1 and 12")
            return
        
        # Validate year input
        if year < 1 or year > 9999:
            print("Error: Year must be between 1 and 9999")
            return
        
        # Create calendar for the specified month and year
        cal = calendar.month(year, month)
        
        # Display the calendar
        print(f"\n{'='*40}")
        print(f"Calendar for {calendar.month_name[month]} {year}")
        print(f"{'='*40}")
        print(cal)
        print(f"{'='*40}")
        
    except ValueError as e:
        print(f"Error: {e}")

# Main program with user input
def main():
    print("🌼 Monthly Calendar Finder 🌼")
    print("=" * 35)
    
    while True:
        try:
            print("\nOptions:")
            print("1. View specific month calendar")
            print("2. View current month calendar")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                # Get month and year from user
                year = int(input("Enter year (e.g., 2024): "))
                month = int(input("Enter month (1-12): "))
                find_calendar(month, year)
                
            elif choice == '2':
                # Show current month
                import datetime
                now = datetime.datetime.now()
                find_calendar(now.month, now.year)
                
            elif choice == '3':
                print("Thank you for using Calendar Finder! 👋")
                break
                
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
                
        except ValueError:
            print("Error: Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

# Enhanced version with more calendar features
def advanced_calendar():
    print("\n🎯 Advanced Calendar Features")
    print("=" * 35)
    
    while True:
        try:
            print("\nAdvanced Options:")
            print("1. View monthly calendar")
            print("2. View yearly calendar")
            print("3. Check if leap year")
            print("4. Get month range")
            print("5. Back to main menu")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                year = int(input("Enter year: "))
                month = int(input("Enter month (1-12): "))
                find_calendar(month, year)
                
            elif choice == '2':
                year = int(input("Enter year: "))
                print(f"\n{'='*50}")
                print(f"Yearly Calendar for {year}")
                print(f"{'='*50}")
                print(calendar.calendar(year))
                
            elif choice == '3':
                year = int(input("Enter year: "))
                if calendar.isleap(year):
                    print(f"🎉 {year} is a LEAP YEAR!")
                else:
                    print(f"{year} is not a leap year")
                    
            elif choice == '4':
                year = int(input("Enter year: "))
                month = int(input("Enter month (1-12): "))
                first_day, num_days = calendar.monthrange(year, month)
                print(f"\nMonth: {calendar.month_name[month]} {year}")
                print(f"First day: {calendar.day_name[first_day]}")
                print(f"Number of days: {num_days}")
                
            elif choice == '5':
                break
                
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Error: Please enter valid numbers!")

# Simple one-time calendar finder
def simple_calendar_finder():
    print("📅 Simple Calendar Finder")
    print("=" * 25)
    
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))
        find_calendar(month, year)
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run different versions
if __name__ == "__main__":
    print("Choose Calendar Program Version:")
    print("1. Simple Version")
    print("2. Full Featured Version")
    print("3. Advanced Version")
    
    version_choice = input("Enter choice (1-3): ").strip()
    
    if version_choice == '1':
        simple_calendar_finder()
    elif version_choice == '2':
        main()
    elif version_choice == '3':
        advanced_calendar()
    else:
        print("Invalid choice! Running full featured version...")
        main()