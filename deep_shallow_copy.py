# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:12:14 2025

@author: ADMIN
"""

#write a python decorator called greet_decorator that adds
#the line hello before calling any function use it on a function 
#say_name() that print "my name is python"

def greet_decorator(func):
    def r():
        print("hello")
        func()
    return r

@greet_decorator
def name():
    print("my name is python")
name()

 
def greet_decorator(func):
    def r():
        print("hello")
        func()
    return r
@greet_decorator
def name():
    print("my name is python")
name()
#create an iterator that returns the square of numbers from 
#1 to 5 using a custom class
no=range(1,6)
square=iter(no)
for n in square:
    print(n**2)



number=range(1,10)
g=iter(number)
for i in g:
    print(i)
    
#write a code example of showing the difference bet shallow copy
#and deep copy using a list of lists.
#modify one inner list after copying and show how each copy 
#is
#affected

import copy
lst=[[10,20,40],[80,90,100]]
sh=copy.copy(lst)
deep=copy.deepcopy(lst)

lst[0][1]=500
print("original list",lst)
print("shallow copy list",sh)
print("Deep copy",deep)


import copy
lst=[[1,2,3,4],[5,6,7,8]]
shallow_copy=copy.copy(lst)
deep_copy=copy.deepcopy(lst)
lst[0][1]=10
print("original list",lst)
print("shallow copy list",shallow_copy)
print("deep copy list",deep_copy)


#create a class car with attributes brand and model and a 
#method
#display() that prints the brand and model of the car create an
#object and call the method
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"brand of car is{self.brand}")
        print(f"model of car is{self.model}")
c=car("TATA","Punch")
c.display()


#write a python script that takes two numbers as a command line
#arguments and print their sum



