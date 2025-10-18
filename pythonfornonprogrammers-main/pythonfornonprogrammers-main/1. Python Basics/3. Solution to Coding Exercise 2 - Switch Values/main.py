#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

  # Assigning Variables

a = 10
b = 20

c = a  # output c = 10
a = b  # output a = 20
b = c  # output b = 10

print("a =",a)
print("b =",b)

print("\n############")

# Tuple way in Most Pythonic way (Mostly Recomended)

a,b = b,a
print("a =", a)
print("b =", b)

print("\n############")

# Using arithmetic operations

a = a + b  # a becomes 30
b = a - b  # b become 10 (30 - 20)
a = a - b  # a becomes 20 (30 - 10)

print("a =", a)
print("b =", b)

print("\n############")

  # Using XOR Operation
  
print(f"Initial: a = {a} ({bin(a)}), b = {b} ({bin(b)})")  

            
                                                             #  a = 01010 (10)
                                                             #  b = 10100 (20)
                                                                  #--------XOR           
a = a ^ b
print(f"Step 1:  a = {a} ({bin(a)}), b = {b} ({bin(b)})") # a becomes  1 1 1 1 0 (30)

                                                               #   a = 11110 (30)
                                                               #   b = 10100 (20)
                                                                   #-------- XOR
b = a ^ b
print(f"Step 2:  a = {a} ({bin(a)}), b = {b} ({bin(b)})") #  b becomes  0 1 0 1 1 (10)



                                                                   #    a = 11110 (30)
                                                                   #    b = 01010 (10)
                                                                      #  -------- XOR
a = a ^ b
print(f"Step 3:  a = {a} ({bin(a)}), b = {b} ({bin(b)})") # a becomes  1 0 1 0 0 (20)

print("a =", a)
print("b =", b)

print("\n############")

  # Using List 
[a, b] = [b, a] 

print("a =", a)  # Output: a = 20
print("b =", b)  # Output: b = 10

print("\n############")

  # Using Dictionary
  
swap = {'a': b, 'b': a}
a, b = swap['a'], swap['b']

print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 20 

print("\n############")

  # One-liner with Function

def swap_values(x, y):
    return y, x

a = 10
b = 20

a, b = swap_values(a, b)

print("a =", a)  # Output: a = 20
print("b =", b)  # Output: b = 10  

print("\n############")

# Using Lambda function 

swap = lambda x, y: (y, x)
a, b = swap(a, b)

print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 20

print("\n############")


   #  For Multiple Variables
   
a = 10
b = 20
c = 30

a, b, c = b, c, a

print("a =", a)  # Output: a = 20
print("b =", b)  # Output: b = 30
print("c =", c)  # Output: c = 10   

