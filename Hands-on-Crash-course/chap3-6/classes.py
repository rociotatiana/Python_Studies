#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:26:23 2021

@author: kala
"""

class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """SImulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
# making an instance from a class

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.name
my_dog.sit()
my_dog.roll_over()

# creating multiple instances

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


class Restaurant():
    """Storing restaurants"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_rest(self):
        print("The restaurant's name is " + self.name.title() + 
              ", and it's known for " + self.cuisine_type + " cuisine." )
    def open_rest(self):
        print(self.name + "'s Restaurant is now open.")
        
domino = Restaurant('domino', 'pizzas')

domino.open_rest()
domino.cuisine_type
domino.describe_rest()

fina_estampa = Restaurant('fina estampa', 'peruvian food')
andes = Restaurant('andes sushi', 'sushi')

fina_estampa.describe_rest()
fina_estampa.open_rest()
fina_estampa.cuisine_type

andes.describe_rest()
andes.open_rest()

class User():
    """Creating an user"""
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
    
    def describe_user(self):
        print("The user's name is " + self.first_name.title() + 
              ". It identifies itself as" + self.sex + " and has " + str(self.age) + " years old.")
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + "!")
        
lara = User('lara' , 'croft', 'female', 35)

lara.describe_user()
lara.greet_user()


carla = User('carla', 'locelace', 'female', 27)

carla.describe_user()
carla.greet_user()


class Car():
    """Attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# putting changeable values
    
class Car():
    """Attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MOdifying attribute values

# directly through an instance

my_new_car.odometer_reading = 23
my_new_car.odometer_reading    

#modifying an attribute's value through a method

class Car():
    """Attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

        
my_new_car.update_odometer(10)

my_new_car.read_odometer()

my_new_car.odometer_reading


### incrementing an attribute's value through a method

class Car():
    """Attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# exercises

class Car():
    """Attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        elif miles < 0:
            print("You can't roll back an odometer!")

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


# MORE EXERCISES

#adding clients
class Restaurant():
    """Storing restaurants"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_rest(self):
        print("The restaurant's name is " + self.name.title() + 
              ", and it's known for " + self.cuisine_type + " cuisine." )
        
    def open_rest(self):
        print(self.name + "'s Restaurant is now open.")
        
    def served_clients(self):
        """Print a statement showing."""
        print("The restaurant has served " + str(self.number_served) + " clients.")
    
    def set_number_served(self, clients):
        if clients >= self.number_served:
            self.number_served = clients
        else:
            print("You can't diminish the number of clients!")
    
    def increment_number_served(self, clients):
        if clients >= 0:
            self.number_served += clients
        elif clients < 0:
            print("You can't diminish the number of clients!")
            
        
domino = Restaurant('domino', 'pizzas')

domino.served_clients()

domino.set_number_served(7)

domino.increment_number_served(5)


class User():
    """Creating an user"""
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print("The user's name is " + self.first_name.title() + 
              ". It identifies itself as" + self.sex + " and has " + str(self.age) + " years old.")
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + "!")
        
    def set_login_attempts(self):
        print("The user has logged " + str(self.login_attempts) + " times.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        
lara = User('lara' , 'croft', 'female', 35)

lara.increment_login_attempts()

lara.set_login_attempts()

lara.reset_login_attempts()


class ElectricCar(Car):
    """Represent aspects of a car, specific too electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
    

class ElectricCar(Car):
    """Represent aspects of a car, specific too electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
        then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()