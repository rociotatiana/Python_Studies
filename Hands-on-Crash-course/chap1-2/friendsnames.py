#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:38:50 2021

@author: kala
"""

friends = ["coni", "nati", "pp", "amanda"]

message1 = "My friend " + friends[0].title() + " is very funny"
message2 = "My friend " + friends[1].title() + " is cool"
message3 = "My friend " + friends[2].title() + " has a beautiful soul"
message4 = "My friend " + friends[3].title() + " is gorgeous"

# como hacer que esto sea más facil y de un tiron


##### shrinking guest list

dinner = ["coni", "amanda", "pp", "joaquin"]

print("Dear friend " + dinner.pop(0).title() + ", I would like to meet you in my wedding.")

#algo más sistemático como una función

#cambiar un invitado

dinner[1] = "nadia"
print(dinner)

#more guests!

dinner.append("laura")
print(dinner)

print("I can only invite 2 people to the weddin")

print("I'm sorry " + dinner.pop() + ", I'm afraid you can't come to the wedding tonight")

print("Dear " + dinner[0].title() + ", you're invited to dinner tonight.")

print("Dear " + dinner[1].title() + ", you're invited to dinner tonight.")

dinner.remove("coni")

dinner.remove("nadia")

print(dinner)