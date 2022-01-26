#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:11:59 2021

@author: kala
"""

x = "mary"
y = "mary"
print (x == y)

x = "mary"
y = x
print (x == y)

x = "Mary"
y = "mary"
print(x == y)
print(x.lower() == y.lower())

x = 15
y = 23
x <=18 and y==23
x <=15 or y == 15

pizzas = ["pesto", "pepperoni", "hawaian"]
order = "napolitana"

order in pizzas
if order not in pizzas:
    print("No tenemos " + order.title() + " en esta sucursal.")

