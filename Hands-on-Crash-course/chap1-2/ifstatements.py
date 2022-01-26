#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:34:24 2021

@author: kala
"""

cars = ["audi", "bmw", "subaru", "toyota"]

#BMW should be upper caps, so we do an if statement when printing

for car in cars: 
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "Audi"
car.lower() == "audi" # TRUE, bc we made case insensitive.

#websites compare usernames in lowercase so the new username won0t match with ANYTHING

# != means NOT EQUAL

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")
    
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
    
age = 19
age < 21
age <= 21
age > 21
age >= 21

# AND expression

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_0 >= 22 and age_1 <= 21

(age_0 >= 22) and (age_1 <= 21)

# OR expression

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >=21

age_0 = 18
age_0 >= 21 or age_1 >= 21

# only 1 condition required for theboolean to be True

# IN expression: checking ifi something is on a list

requested_toppings = ["mushrooms", "onions", "pineapple"]
"mushrooms" in requested_toppings

"pepperoni" in requested_toppings

#NOT expressions, checking if someone is NOT in a list

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

car = "subaru"
print("Is car == 'Subaru?' I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")


