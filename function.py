# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 18:26:34 2025

@author: ADMIN
"""
#simple function
def my_fun():
    print("hello ishwari")
my_fun()
#hello ishwari
 
#function with argument

def my_fun(name):
    print("hello"," " +name)
my_fun("ishu")
#hello  ishu

def f(ag):
    print("hii" " "+ag)
f("ishu")
#hii ishu
#function with positional argument
def my_fun(name,name1):
    print(name+" "+name1)
my_fun("helloo","world")
my_fun("world","hello")
'''
helloo world
world hello'''

def s(l1,l2):
    print(l1+" "+l2)
s("Manoj","ishwari")
#Manoj ishwari

#fun with arbitrary arguments, *args
#if you dont know how many arguments
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("Tappu","sonu","soni")
#Tappu soni
def r(*a):
    print(a[1]+" "+a[3])
r("sakshi","sujata","samruddhi","sanika")
#sujata sanika
#for key value in function use kwargs
def myfun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
myfun(first_name='popalal',mid_name='mohanlal',last_name='goyal')
'''
first_name:popalal
mid_name:mohanlal
last_name:goyal
'''
"""
**kwargs collects all keyword arguments into a dictionary.
kwargs.items() returns a list of (key, value) tuples from that dictionary.
The for loop iterates through these items and prints each key-value pair in the format key:value.

"""

def my_function(country="norway"):
    print("i am from"+country)
my_function("india")
my_function("brazil")
my_function("london")
my_function()


def college(name="sanjivani"):
    print("i am from"+name)
college("amrutvahini")
college("Pravara")
college("MIT")
college("Matoshri")
college("SND")
college()

fruits=["orange","banana","guava"]
def my_fun(fruits):
    for x in fruits:
        print(x)
my_fun(fruits)
'''
orange
banana
guava
'''

#function return a value
def my_fun(x):
    y=x*5
    return y
my_fun(5)
#25
def r(x):
    a=x+2
    return a
r(0)
#2
def my_function(x):
    y=x*5
    z=x*7
    return y,z
my_function(5)
#(25,35)
def op(x,y):
    a=x*y
    b=x+y
    c=x/y
    d=x-y
    return a,b,c,d
op(4,2)
#pass function
def my_function():
    pass
my_function()

def pasw(v):
    #pass
    f=v-1
    return f
    pass
pasw(1)
