#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 00:03:03 2021

@author: kala
"""

for value in range(1,5):
    print(value)
    
numbers = list(range(1,6))
print(numbers)      # an array is made

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# VERSION MEJORADA

squares= []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#EXPERIMENTO

halfs = []
for value in range(2,8,2):
    half = value/2
    halfs.append(half)

print(halfs)

# mejorar experimento

halfs = []
for value in range(2,8,2):
    halfs.append(value/2)
    print(halfs)
print(halfs)

### STATS

num_stat = list(range(0, 10))
print(num_stat)

#LIST COMPREHENSION

squares = [value**2 for value in range(1,11)]
print(squares)

halfs = [value/2 for value in range(2,8,2)]
print(halfs)

# EXERCISES

twenties = []
for value in range(1,21):
    twenties.append(value)
print(twenties)

hundreds = []
for value in range(1,101):
    hundreds.append(value)
print(hundreds)
    
thousands = []
for value in range(1,1001):
    thousands.append(value)
print(thousands)

oddies = []
for value in range(1, 20, 2):
    oddies.append(value)
print(oddies)

threes = []
for value in range(1,11):
    threes.append(value*3)
print(threes)

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#list comprehension
cubies = [value**3 for value in range(1,11)]
print(cubies)
