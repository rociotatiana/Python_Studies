#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:39:09 2021

@author: kala
"""

def make_pizza(*toppings):
    """SUmmarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
    