#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:50:21 2021

@author: kala
"""
## Modifying elements in a list

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0]= "ducati"
print(motorcycles)

## ADDING elements to a list

#append()
motorcycles.append("ducati")
print(motorcycles) #adds it at the end

#insert()

motorcycles.insert (0, "ducati")
print(motorcycles) #opens a space in 0 and places ducati, shifting all other positions to the right

##REMOVING elements of a list

#del

del motorcycles[1]
print(motorcycles) #2d moto removed from the list

#pop()

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) #pop() lets your work with the erased element even after its erased


# LAST MOTORCYCLE I HAD
# if list is in chronological order, i can use pop to know my last moto

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#popping from any positiion

first_owned = motorcycles.pop(0)
print("The firt motorcycle I owned was a " + first_owned.title() + ".")

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove ("ducati")
print(motorcycles)

#####

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

