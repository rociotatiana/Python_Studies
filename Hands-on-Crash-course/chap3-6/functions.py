#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:29:44 2021

@author: kala
"""

def greet_user():
    """Display a simple greeting"""
    print("Hello!")
    
greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print( "Hello, " + username.title() + "!")

greet_user('jesse')

def display_message():
    """What I learned at chapter 8"""
    print("I'm learning about functions, which are named blocks of code designed to do one specific thing")

display_message()

def favorite_book(book):
    print("One of my favorite book is " + book.title() + ".")
    
favorite_book('Dune')

# pets

def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('perro', ' frida' )
describe_pet('gata', 'matilde')

describe_pet(pet_name='harry', animal_type='hamster')

# default values

def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name = 'wullie')
describe_pet('willie')
describe_pet('wilie', 'cat')

describe_pet()

def make_shirt(size, text): 
    print("Order: a shirt size " + size.title() + ", with the following text: '" + text.title() + "'.")
    
make_shirt('s', 'carpe diem')

make_shirt('m', 'eren yeager was wrong')

def make_shirt_python(size='m', text='i love python'): 
    print("Order: a shirt size " + size.title() + ", with the following text: '" + text.title() + "'.")

make_shirt_python()

make_shirt_python(size='l', text='CSS the best')

def describe_city(city, country = 'Chile'):
    print(city.title() + " is in " + country.title())
    
describe_city('concon')
describe_city(city='oruro', country='bolivia')

# return values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

get_formatted_name('jimi', 'hendrix')
musician= get_formatted_name('jimi', 'hendrix')
print(musician)

# middle name included

def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'hooker' , 'lee')
print(musician)


# returning a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last' : last_name}
    return person

build_person('carla', 'solar')

musician = build_person('jimi', 'hendrix')
print(musician)

#####

def pets( animal, pet_name):
    pets = {'animal': animal, 'name': pet_name}
    return pets

pets('hamster' , 'bernie')

# ####

def build_person(first_name, last_name, age= ''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# while loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
# city names
    
def city_country(city, country):
    print(city.title() + ', ' + country.title())

city_country('Concepción', 'Chile')
city_country('valdivia', 'chile')
city_country('la paz', 'bolivia')

# make a album

def make_album(artist, album_title):
    """Return a dictionary of info about an album"""
    album = {'artist': artist, 'album_title': album_title}
    return album

taylor = make_album('taylor swift', 'idk')

print(taylor)

#tracks version

def make_album(artist, album_title, tracks = ''):
    """Return a dictionary of info about an album"""
    album = {'artist': artist, 'album_title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

taylor = make_album('taylor swift', 'idk', 8)

print(taylor)

# user input
def make_album(artist, album_title):
    """Return a dictionary of info about an album"""
    album = {'artist': artist, 'album_title': album_title}
    return album

while True:
    print("Tell about an album that you like:")
    print("(enter 'q' at any time to quit)")
        
    this_artist = input("Artist name: ")
    if this_artist == 'q':
        break
    this_album_title = input("Album name: ")
    if this_album_title == 'q':
        break
    this_album = make_album(this_artist, this_album_title)
    print("This is the dictionary we created: ")
    print(this_album)
    

# passing a list
    
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# modifying a list in a function

# star with some desing that need to be printed.

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    
# Simulate creatin a 3D print from the desing.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models: 
    print(completed_model)
    
# Improving efficiency


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Simulate creating a 3D print from the design.
        print("PRinting model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Magicians

magicians = ['phil', 'lucas', 'claire', 'andy', 'edo caroe']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
        
show_magicians(magicians)

def make_great(magicians):
    for magician in magicians:
        magician = "the Great " + magician.title()
        print(magician)
        
make_great(magicians)
# it wasn't modified.

## passing an arbitrary number of arguments

def make_pizza(*toppings):
    """SUmmarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
    
make_pizza('pepperoni', 'cheese', 'olives', 'avocado')

# arbitrary keyword arguments

def build_profile(first, last, **user_info):
    """ BUild a dictionary containing everything we know about a user."""
    profile ={}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', 
                             field = 'physics')
print(user_profile)


# sandiwhes

def make_sandwich(*ingredients):
    print("\nWe are making a sandwich for you with the following ingredients that you asked: ")
    for ingredient in ingredients:
        print( "- " + ingredient.title())
        
make_sandwich('pesto', 'tomato', 'avocado', 'lettuce', 'pickles')

user_profile = build_profile('rocío', 'perez', pets =  ' frida and sofia' , 
                             city = 'san pedro de la paz')
print(user_profile)

# cars

def make_car(car_brand, car_type, **car_info):
    car = {}
    car['brand'] = car_brand
    car['type'] = car_type
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color= 'blue', tow_package=True)
print(car)

import pizza

pizza.make_pizza('pepperoni', 'mushrooms')

from pizza import make_pizza

from pizza import make_pizza as mp
