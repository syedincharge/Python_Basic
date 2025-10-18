#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Project 4 - Bill Roulette


import random

names_string = input("Input everyone's name, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_int = random.randint(0, num_items-1)

person_name = names[random_int]

print(f"{person_name} is going to buy the meal today!")