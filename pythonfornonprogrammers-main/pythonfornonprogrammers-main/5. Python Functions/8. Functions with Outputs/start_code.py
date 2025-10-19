import math




# Functions with Outputs

def my_first_function():
    """This is my first function which does not take any parameters but returns a value."""
    return 1 + 2

result = my_first_function()
print(f"Result of my_first_function: {result}")


math.sqrt(16)
print(f"Square root of 16 is: {math.sqrt(16)}")

def print_twice():
    """Print a message twice."""
    print("This message is printed twice.")
    print("This message is printed twice.")
    
output = print_twice()
print(f"Output of print_twice function: {output}")    

    

def format_name(f_name, l_name):
    """Take first and last names and format them to title case."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    full_name = f"{f_name} {l_name}"
    return full_name.title() 

# Example usage: pass the first and last name as separate strings
formatted_name = format_name("syed", "rizvi")
print(f"Formatted name: {formatted_name}")

