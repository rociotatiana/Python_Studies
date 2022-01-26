#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:52:34 2021

@author: kala
"""

#alien colors

alien_color = ["green", "yellow", "red"]

color= "green"

if color in alien_color:
    print("The alien is green! You just earned 5 points")
else:
    print()
    
alien_color = ["green", "yellow", "red"]

color= "pink"

if color in alien_color:
    print("The alien is green! You just earned 5 points")
else:
    print()
    


alien_color = ["green", "yellow", "red"]

color= "green"

if color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
    
    
alien_color = ["green", "yellow", "red"]

color= "pink"

if color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
    
### EXERCISE


alien_color = ["green", "yellow", "red"]

color= "green"

if color in alien_color and color == "green":
    print("You just earned 5 points!")
elif color in alien_color and color != "green":
    print("You just earned 10 points!")
elif color not in alien_color:
    print("This color can't happen!")
    
    
alien_color = ["green", "yellow", "red"]

color= "pink"

if color in alien_color and color == "green":
    print("You just earned 5 points!")
elif color in alien_color and color != "green":
    print("You just earned 10 points!")
elif color not in alien_color:
    print("This color can't happen!")
    
# IF GREEN 5 POINTS, IF YELLOW 10 POINTS, IF RED 15 POINTS
    
alien_color = ["green", "yellow", "red"]

color= "red"

if color in alien_color and color == "green":
    print("You just earned 5 points!")
elif color in alien_color and color == "yellow":
    print("You just earned 10 points!")
elif color in alien_color and color == "red":
    print("You just earned 15 points!")
elif color not in alien_color:
    print("This color can't happen!")
    
# STAGES OF LIFE

age = 15

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65: 
    print("You are an adult.")
elif age >= 65: 
    print("You are am elder.")
    
# FAV FRUITS
    
fav_fruits = ["frutilla", "nispero", "sandia"]

if "frutilla" in fav_fruits: 
    print("Realmente me gustan las frutillas")
else:
    ("No me gustan las frutillas")
if "melon" in fav_fruits:
    print("Realmente me gustan los melones")
else:
    print("No me gustan los melones")
if "nispero" in fav_fruits: 
    print("Amo los nisperos!")
else:
    print("No me gustan los nisperos")
if "naranjas" in fav_fruits:
    print("Ñom ñom a las naranjas")
else: 
    print("Ñom ñom'nt a las naranjas")
