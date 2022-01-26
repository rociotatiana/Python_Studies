#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:31:43 2021

@author: kala
"""

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title()) #agrega mayuscula al final
print(bicycles[-1]) #return last element of the list

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)