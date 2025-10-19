#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Functions with inputs

def greet():
    print("Hello Elshad")
    print("How are you Elshad?")

# greet()

# Function with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}")
    
#greet_with_name("Syed")


def greet_with_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print(f"How are you {first_name} {last_name}")
greet_with_full_name("Syed", "Rizvi")


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")



def greet_with_Name_location(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with_Name_location("Syed", "New York")    
    
    
# create function with more postional arguments with examples
def greet_with_details(name, location, age):
    print(f"Hello {name}")
    print(f"You are {age} years old")
    print(f"What is it like in {location}?")
greet_with_details("Syed", "New York", 25)


# create function with keyword arguments
greet_with_details(age=30, location="California", name="Alice")
# Call the functions with different inputs to demonstrate their functionality
greet_with_name("Charlie")
greet_with_Name_location("David", "Texas")
greet_with_details("Eve", "Florida", 28)
greet_with_details(location="Washington", name="Frank", age=35)
greet_with_full_name("John", "Doe")
greet_with_full_name("Jane", "Smith")
greet_with_name("Grace")
greet_with_Name_location("Hannah", "Ohio")
greet_with_details("Ian", "Nevada", 40)
greet_with_details(age=22, name="Jack", location="Oregon")
greet_with_details(location="Michigan", age=29, name="Kathy")
#   Created by Syed Rizvi


