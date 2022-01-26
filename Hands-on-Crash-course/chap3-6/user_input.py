#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:47:33 2021

@author: kala
"""

message = input("Tell me something, and I wil repeat it back to you: ")
print(message)

# greeter

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your firt name? "

name = input(prompt)
print("\nHello, " + name + "!")

# int() function

age = input("How old are you?" )
age = int(age)
age >= 18

# rollercoaster

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else: 
    print("\nYou'll be able to ride when you're a little older." )
    
# oddie or even
    
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
    
# EXERCISES

# rental car

car = input("What kind of rental car would you like to rent? ")

print("Let me see if I can find you a " + car + ".")

# restaurant seating

seats = input("How many people are in your dinner group? ")
seats = int(seats)

if seats > 8:
    print("You'll have to wait for a table.")
else: 
    print("Your table is ready!")

# multiples of ten

number = input("Tell me a number and I'll tell if its multiple of 10 or not. ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not multiple of 10.")
    

# while loop

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# parrot with quit option

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit'to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    
# improvement

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit'to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit'to end the program. "

active = True
while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else: 
        print(message)

# break to exit loop
        
prompt = "\nPLease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: 
    city = input(prompt)
    
    if city == 'quit':
        break
    else: 
        print("I'd love to go to " + city.title() + "!")
        

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
 
# PIZZA ORDERRRS
    
prompt = "\nThank you for ordering in Rous's Pizza"
prompt += "\nWhat toppings would you like for your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

while True: 
    topping = input(prompt)
    
    if topping == 'quit':
        print ("Your pizza ordering is ready!")
        break
    else: 
        print("Adding " + topping + " to your pizza.")
        
# tickets
    
prompt = "Welcome to Rous's Theater, we have different prices according to age" 
prompt += "\nCould you tell us how old are you? "

while True: 
    age = input(prompt)
    age = int(age)
    
    if age < 3:
        ticket = 0
    elif age >= 3 and age <= 12:
        ticket = 10
    elif age > 12:
        ticket = 15
    
    print("The cost of your ticket is $" + str(ticket) + ".")
    break

### LOOPS & DICTIONARIES & LISTS
    
##° moving items from 1 list to another
    
# start with users that need to be verified, 
    #and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each unconfirmed user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print ("Verifying user : " + current_user.title())
    confirmed_users.append(current_user)
#Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
   
    # rREMOVING ALL INSTANCES OF A SPECIFIC VALUE FROM A LIST
# pets
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

dojo = ['paola', 'carla', 'cami', 'paola', 'miguel', 'nico', 'ricardo', 'paola', 
        'pato', 'paola', 'jona', 'paola', 'nico' ]
print(dojo)

while 'paola'in dojo:
    dojo.remove('paola')
while 'nico'in dojo:
    dojo.remove('nico')

print(dojo)

# filling dictionaries with user input

responses = {}

# set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    #prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # sotre responses in dictionary
    responses[name] = response
    
    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
#Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    
# EXERCISES
    
# deli

sandwich_orders = ['barros luco', 'pastrami', 'mamaterra', 'falafel',
                   'pastrami', 'mamaterra']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Realizando su pedido de sandwich de " + current_sandwich.title())
    finished_sandwiches.append(current_sandwich)

print("\nHemos preparado los siguientes sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
    
# no hay pastrami
    
sandwich_orders = ['barros luco', 'pastrami', 'mamaterra', 'falafel',
                   'pastrami', 'mamaterra']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if 'pastrami'in current_sandwich:
        print("Lo siento, nos hemos quedado sin stock de " + current_sandwich.title())
        continue
    else: 
        print("Realizando su pedido de sandwich de " + current_sandwich.title())
        finished_sandwiches.append(current_sandwich)

print("\nHemos preparado los siguientes sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())