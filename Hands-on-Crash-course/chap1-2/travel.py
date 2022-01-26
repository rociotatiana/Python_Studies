#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:42:01 2021

@author: kala
"""

places = ["mexico", "canada", "islandia", "japon"]

print(places) # print en orden originial

print(sorted(places)) # print en orden alfabetico

print(places) # a pesar de la linea anterior, la lista sigue en el mismo orden

print(sorted(places, reverse=True)) # 

print(places)

places.reverse()

print(places)

print(sorted(places))
