#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Project 3 - Leap Year with Function

year = int(input("Enter year: "))

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year."
            else:
                return "Not leap year"
        else:
            return "Leap year."
    else:
        return "Not leap year."
  

print(leap_year(year))
