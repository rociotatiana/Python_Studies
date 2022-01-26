#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:34:53 2021

@author: kala
"""

## WROKING WITH PARTS OF A LIST

#slicing a list

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

print(players[:4]) # if you omit index, it starts in the beginning of the list.
print(players[2:]) # if you don't pput theend, it will end on the end of the elements.

print(players[-3:]) #output the last 3 players in the roster
# looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
# copying a list

my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods [:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_foods)

#adding food

my_foods.append("cannoli")
friends_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_foods)

#if you homologue 2 variables it won't work to try to append things on it. Better use slice for that.

###EXERCISES

print("The first three items in the list are:")
print(my_foods[:3])

print("The middle items in the list are:")
print(my_foods[1:3])

print("The last three items in the list are:")
print(my_foods[1:])

## EXERCISES

pizzas = ["pepperoni", "napotilana", "hawaiana"]
friend_pizzas = pizzas [:]

pizzas.append("pesto")
friend_pizzas.append("sevillana")

print("These are the pizzas I like:")
print(pizzas)

print("\nAnd these are the pizzas my friend likes:")
print(friend_pizzas)

for pizzas in pizzas:
    print(player.title())
    
#arreglao

print("These are the pizzas I like:")
for pizza in pizzas:
    print(pizza.title())

print("\nAnd these are the pizzas my friend likes:")
for pizza in friend_pizzas:
    print(pizza.title())


# TUPLES immutable lists

dimensions = (200, 50) # () assure us that it won't be changed
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignments

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#if we want to change it, we must redefine the tuple entirely, writing over it

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions: 
    print(dimension)

# buffet
buffet = ("paella", "rissoto", "papas fritas", "porotos", "cazuela")

buffet[2] = "chunchules"    

print("Original menu:")
for food in buffet:
    print(food.title())

buffet = ("paella", "asado", "chunchule", "porotos", "cazuela")

print("\nModified menu:")
for food in buffet:
    print(food.title())
