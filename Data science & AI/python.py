#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 01:34:24 2021

@author: kala
"""

A = "Michael Jackson is the best"

B = A.replace("Michael", "Janet")

#Method find

name = "Michael Jackson"

name.find('el')

name.find('Jack')

name[0:4]

name[::2]

NT = (1, 2, ('pop', 'rock'), (3, 4), ('disco', (1, 2)))

NT [2] [1]

# WEEK 2: LISTS

L = ["Michael Jackson", 10.1, 1982]
L

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


# Sample List: List contents, integers, floats, strings, tuples and lists

["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]


# List operations

L = ["Michael Jackson", 10.1,1982,"MJ",1]
L

# List slicing

L[3:5]


# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space

'hard rock'.split()

# Split the string by comma

'A,B,C,D'.split(',')


# COPY AND CLONE LIST


# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])


# Clone (clone by value) the list A

B = A[:]
B

# if you change A, B will not change

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])



## TUPLES

# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1

# Print the type of the tuple you created

type(tuple1)

# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element

tuple1[-1]

# Use negative index to get the value of the second last element

tuple1[-2]

# Use negative index to get the value of the third last element

tuple1[-3]

# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2

# Slice from index 0 to index 2

tuple2[0:3]

# Slice from index 3 to index 4

tuple2[3:5]

# Get the length of tuple

len(tuple2)

# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# As we can't change the tuples, We can sort the values in a tuple and save it to a new tuple:

# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted


# Create a nest tuple: holding complex values

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


#We can access the nested tuples:
# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# We can access strings in the second nested tuples using a third index:
# Print the first element in the second nested tuples

NestedT[2][1][0]

# Similarly, we can access elements nested deeper in the tree with a third index:
# Print the first element in the second nested tuples

NestedT[4][1][0]

# Print the second element in the second nested tuples

NestedT[4][1][1]


# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

len(genres_tuple)

genres_tuple[3]

genres_tuple[3:6]

genres_tuple[0:2]

#find the first index of 'disco':
genres_tuple.index('disco')


artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)



# EXCEPTION HANDLING

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        
    
    
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
        



a = 1

try:
    b = int(input('Please enter a number to divide a: '))
    a = a/b
    print('Success! a = ', a)
except ZeroDivisionError:
    print('The number you provided cant divide 1 because it is 0')
except ValueError:
    print('Your did not provide a number')
except:
    print('Something went wrong')
    

# Import the library

import matplotlib.pyplot as plt
%matplotlib inline  
# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
        
        
# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
        
class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0


-------


# Creating files


with open ("Example1.txt", "w") as File1:
    File1.write("This is line A")
    
    
Lines = ['This is line A\n', 'This is line B\n', 'This is line C\n', 'This is line D\n']

with open ("Example2.txt", "w") as File1:
    for line in Lines:
        File1.write(line)
    
#appending
        
with open ("Example1.txt", "a") as File1:
    File1.write("\nThis is line B")
    
#copying files
with open ("Example2.txt", "r") as readfile:
    with open ("examples3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)
            
            
            
#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            #go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()
                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
    
    
    
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    