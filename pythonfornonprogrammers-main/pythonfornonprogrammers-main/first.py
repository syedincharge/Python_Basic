print("What will be the output of the following function calls? Explain your answer.")

def my_function(a):
    if a < 20:
        print("Bad")
        return "Bad"
    elif a < 80:
        print("Passed") 
        return "Passed"
    else:
        print("Good")
        return "Good"

print(my_function(10))  # Output: Bad
#print(my_function(50))  # Output: Passed  
#print(my_function(90))  # Output: Good  