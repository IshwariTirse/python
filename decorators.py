# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 09:58:08 2025

@author: ADMIN
"""
#pre-requisite to decorators
def plus_one(number):
    number1=number+1
    
#function insidefunction
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    
    result=add_one(number)
    return result
plus_one(4)

#passing function as argument
#to other functions
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)

#function returning other functions
def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi
#hello function
hello=hello_function()
hello()

import time
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution square is{total_time}")
    return result
#A python decorator is a function 
#that takes in a function and
#returns it by adding some functionality
def say_hi():
    return "hello there"
def uppercase_decorators(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorators(say_hi)
decorate()

#uppercase decorators
@uppercase_decorators
def say_hi():
    return "hello there"
say_hi()

def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorators(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@split_string
@uppercase_decorators
def say_hi():
    return "hello there"
say_hi()


import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__+"took" +
              str((end-start)*1000)+"mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
        return result
    