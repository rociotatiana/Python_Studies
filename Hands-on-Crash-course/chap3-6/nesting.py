#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:17:17 2021

@author: kala
"""

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
## Making a fleet of 30 aliens
    
# empty list
aliens = []

# mañe 30 gren aliens

for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens
    
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]: 
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:3]: 
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
## PIZZA
pizza = { 'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'], }

# summarize order
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# laguages
    
fav_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'], 
        'phil': ['python', 'haskell']}

for name, languages in fav_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
        
for name, languages in fav_languages.items():
    if (len(languages)) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    elif (len(languages)) == 1:
        print("\n" + name.title() + "'s favorite language is " + language.title())

# USERS

users = {
        'aenstein': {
                'first': 'albert',
                'last': 'einstein',
                'location': 'princeton',
                }, 
        'mcurie': {
                'first': 'marie',
                'last': 'curie',
                'location': 'paris',
                },
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    
# EXERCISES
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
#pets
    
pets = {
        'ambar': { 
                'dueña': 'mamá',
                'color': 'amarillo',
                'raza': 'quiltra', 
                'edad': '3 años',
                'sexo': 'hembra',},
        'frida': { 
                'dueña': 'rocío', 
                'color': 'blanco', 
                'raza': 'fox terrier',
                'edad': '10 años',
                'sexo': 'hembra',}
        }

for perro, info_perro in pets.items():
    print(perro.title() + " es una perra " + info_perro['sexo'] + " de raza " + 
          info_perro['raza'] + " cuya dueña es " + info_perro['dueña'].title() +
          ", tiene " + info_perro['edad'] + " de edad, y es de color " +
          info_perro['color'])
    
# favorite places

fav_places = { 'mamá': 'sta barbara', 
              'miguel': 'cama',
              'rocío': 'san pedro'}

for name, places in fav_places.items():
    print("El lugar favorito de " + name.title() + " es " + places.title() )
    
fav_numbers = {'stephi': [4, 7],
               'mamá': [7, 1],
               'miguel': [19, 5],
               'antu': 3, 
               'rocío': 9}

for name, numbers in fav_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    print("\t" + str(numbers))
    
# comparar con el siguiente
for name, numbers in fav_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    print("\t" + str(numbers))
    
# cities

cities = { 
        'san pedro': {
                'población': 'media', 
                'país': 'chile',
                'dato': 'tiene 2 lagunas muy cercanas entre sí',},
        'roma': { 
                'población': 'grande',
                'país': 'italia',
                'dato': 'solía ser una superpotencia política'},
        'new york': { 
                'población': 'muy grande',
                'país': 'estados unidos', 
                'dato': 'es la ciudad del sueño americano'}
    
}

for city, city_info in cities.items(): 
    print("La ciudad de " + city.title() + " pertenece a " + 
          city_info['país'].title() + " y tiene una población " +
          city_info['población'] + ", es reconocida porque " +
          city_info['dato'])
    
