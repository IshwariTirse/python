# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 09:39:23 2025

@author: ADMIN
"""
gen=(x for x in range(3))
next(gen)
next(gen)

#function with multiple values



#let us hide password entered on screen 
#chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["not-good","give m-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
 
#enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
    
#same code can be implemented using enumerate
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")

#use of zip it wont display baba
name=["dada","kaka","mama","baba"]
info=[9850,6032,9785]
for nm, inf in zip(name,info):
    print(nm,inf)
    
#zip longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm, inf in zip_longest(name,info):
    print(nm,inf)
    
#use of fillvalue instead of none
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm, inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

#values must be non zero, +ve or -ve
lst=[2,3,-6,8,9]
if all(lst):
    print("all values are true")
else:
    print("there are null values")
    
lst=[2,3,0,8,9]
if all(lst):
    print("all values are true")
else:
    print("there are null values")

#use of any
lst=[0,0,0,0,0]
if any(lst):
    print("It has value")
else:
    print("all values are null in list")

from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

#lets start with 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#cycle
import itertools
instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
    
    
#repeat
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)
#it will show msg for three times



