#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

def my_first_function():
    print("Hello, I am a function") 
    print("See you later, Bye for now")

my_first_function()
my_first_function()


def my_second_function():
    """This is my second function which does not take any parameters and does not return any value."""
    print("This is my second function")
    print("I am happy to learn Python functions")
      
    
    # Call the second function to show its output
my_second_function()



# Function to demonstrate if and elif statements
def check_number(number):
    if number > 0:
        print(f"{number} is a positive number")
    elif number == 0:
        print("Number is zero")
    else:
        print(f"{number} is a negative number")

# Multiple examples to demonstrate if / elif / else
examples = [10, 0, -5, 42, -100]
for num in examples:
    check_number(num)


     
     