#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:25:42 2021

@author: kala
"""
# Checking for especial items
requested_toppings = ["mushrooms", "green peppers", "extracheese"]

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#OUT OF GREENPEPPER

requested_toppings = ["mushrooms", "green peppers", "extracheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# CHECKING IF THE LIST'S EMPTY 


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers":
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
# USING DIFFERENT LISTS
    
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

#EXERCISE

alien_color = ["green", "yellow", "red"]

colors= ["red", "pink", "yellow"]

for color in colors:
    if color == "green": 
        point = 5
    if color == "yellow": 
        point = 10
    if color == "red": 
        point = 15
    if color in alien_color:
        print("A " + color + " alien! You just earned " + str(point) + " points")
    else:
        print("This color can't happen!")
# CÓMO PUEDO RECOLECTAR LOS NUMEROS Y SUMARLOS AL FINAL DEL CICLO?
    
#### EJERCICIOS
        
        
usernames = ['lisa', 'nero', 'admin', 'cali', 'luis']
usernames = []

for user in usernames:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status report?")
    else: 
        print("Hello " + user.title() + ", thank you for logging in again.")
        
if usernames: 
    for user in usernames:
        if user == 'admin':
            print("Hello " + user.title() + ", would you like to see a status report?")
        else: 
            print("Hello " + user.title() + ", thank you for logging in again.")
else: 
    print("We need to find some users!")
    
    
# checking users
    
current_users = ['lisa', 'nero', 'admin', 'cali', 'luis']

new_users = ['julio', 'pepe', 'coni', 'amanda', 'Lisa', 'cali']

current_users.lower()

sorted(new_users)

for user in current_users:
    user = user.lower()
for user in new_users:
    user = user.lower()
    if user in current_users:
        print("Username " + user + " in use. Pick a new username.")
    else: 
        print("Username " + user + " available.")
# no pude hacer uno sin modificar los valores de Mayusculas y minusculas.

ordinals = list(range(1,10))
print(ordinals)

for n in ordinals:
    if n == 1:
        print(str(n) + "st")
    elif n == 2:
        print(str(n) + "nd")
    elif n == 3:
        print(str(n) + "rd")
    elif n >= 4 and n <10:
        print(str(n) + "th")
