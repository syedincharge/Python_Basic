#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Custom Function in Loop

def password_controller(password):
   if len(password) > 8:
       return True
   else:
       return False

print(password_controller("123456789"))