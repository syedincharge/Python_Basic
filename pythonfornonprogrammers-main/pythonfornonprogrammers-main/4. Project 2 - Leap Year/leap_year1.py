#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

#     Leap Year


print("Program to find the leap year \n")

year = int(input("Enter the Year \n"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")
  