#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Project 3 - Leap Year with Function

def leap_year(p_year):
    if p_year % 4 == 0:
       if p_year % 100 == 0:
         if p_year % 400 == 0:
             return "Leap year."
         else:
             return "Not leap year."
       else:
           return "Leap year."
    else:
        return "Not leap year."
      
print("Program to find the leap year \n")
year = int(input("Enter the Year \n"))
print(leap_year(year)) 

