#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com
#               Leap Year

print("Program to find the leap year \n")

year = int(input("Enter the Year \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")    
    else:
        print("This is Leap Year")
else:    
      print("Not Leap Year.")
    






       