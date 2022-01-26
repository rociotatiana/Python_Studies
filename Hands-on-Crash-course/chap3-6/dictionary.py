#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:12:50 2021

@author: kala
"""

alien_0 = {'color' : 'green' , 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print("you just earned " + str(alien_0['points']) + " points!")

new_points = alien_0['points']

print("you just earned " + str(new_points) + " points!")

# adding new key values

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# doing an ampty dictionary

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10

# modifying values

alien_0['color'] = 'red'


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# MOve the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# fast alien

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))

# MOve the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# y movement
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original y-position: " + str(alien_0['y_position']))

# MOve the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    y_increment = 3
elif alien_0['speed'] == 'medium':
    y_increment = 6
else:
    # This must be a fast alien
    y_increment = 9

# The new position is the old position plus the increment.
alien_0['y_position'] = alien_0['y_position'] + y_increment

print("New y-position: " + str(alien_0['y_position']))

# removing key-value pairs

alien_0 = {'color' : 'green' , 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# DICTIONARY OF SIMILAR OBJECTS

fav_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'}

print("Sarah's favorite language is " + 
      fav_languages['sarah'].title() +
      ".")


# EXERCISES

hermano = {'nombre': 'miguel',
           'apellido': 'pérez',
           'ciudad': 'stgo'}

print("Mi hermano se llama " + hermano['nombre'].title() + " " +
      hermano['apellido'].title())
print("Vive en " + hermano['ciudad'].title())


#numeros fav

fav_numbers = {'stephi': 4, 
               'mamá': 7,
               'miguel': 19, 
               'antu': 3, 
               'rocío': 9}

print("El número favorito de Stephi es " + str(fav_numbers['stephi']))
print("El número favorito de Mamá es " + str(fav_numbers['mamá']))
print("El número favorito de Stephi es " + str(fav_numbers['stephi']))

fav_numbers = {'stephi': 4, 
               'mamá': 7,
               'miguel': 19, 
               'antu': 3, 
               'rocío': 9}

for key, value in fav_numbers.items():
    print("El número favorito de " + key.title() + " es " + str(value))

# looping through key value pairs

user_0 = {'username': 'efermi', 
          'first': 'enrico', 
          'last': 'fermi'}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
    
# languages ex
    
fav_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'}

for name, language in fav_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
    
for name in fav_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in fav_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
              ", I see your favorite language is " +
              fav_languages[name].title() + "!")
        
# numbers ex
fav_numbers = {'stephi': 4, 
               'mamá': 7,
               'miguel': 19, 
               'antu': 3, 
               'rocío': 9}

brothers = ['antu', 'miguel']

for name in fav_numbers.keys():
    print(name.title())
    
    if name in brothers:
        print(" Hi " + name.title() +
              ", I see your fav number is " + str(fav_numbers[name]) + "!")
if 'erin' not in fav_numbers.keys():
    print("Erin, please take our poll!")
for name in sorted(fav_numbers.keys()):
    print(name.title() + ", thank you for answering the poll.")
    
## Looping through values
    
fav_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'}

print("The following languages have been mentioned:")
for language in fav_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(fav_languages.values()):
    print(language.title())
    
# nambers
    
print("The following numbers have been mentioned:")
for number in fav_numbers.values():
    print(number())

# EXERCISESSSS

# rivers
    
rivers = {'nilo': 'egipto',
          'orinoco': 'amazonas', 
          'biobio': 'chile'}
for river, country in rivers.items():
    print("El río " + river.title() + " corre a través de las tierras de " + 
          country.title() + ".")
    

print("Ríos: ")
for river in rivers.keys():
    print(river.title())

print("Países: ")
for country in rivers.values():
    print(country.title())
    
