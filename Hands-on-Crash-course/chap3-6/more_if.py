#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:32:34 2021

@author: kala
"""

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: 
    print("You can't vote yet.")
    print("Please register to vote as soon as you turn 18!")
    
    
# IF ELIF ELSE
    
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18: 
    print("Your admission cost is $5.")
else: 
    print("Your admission cost is $10.")
    
# IMPORVING THE CODE
    
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# ADDING MORE ELIFS

age = 76

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# OMITING THE ELSE CONDITION

age = 76

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")


## MORE THAN 1 CONTDITIONS

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese")
    
print("\nFInished making your pizza!")


# TRYING ELIF 

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese")
    
print("\nFInished making your pizza!") # only adds mushrooms



