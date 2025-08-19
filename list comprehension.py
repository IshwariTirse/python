# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 09:23:22 2025

@author: ADMIN
"""

list=[]
for num in range(0,20):
    list.append(num)
print(list)

lst=[num for num in range(0,20)]
print(lst)

#to capital first letter
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)

#list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

#for inside for loop
lst=[f"{x}:{y}" for x in range(3) for y in range(3)]
print(lst)

#set-carries unique number
#set comprehension
set_one={x for x in range(3)}
print(set_one)

#Dictionary comprehension
dict={x:x*x for x in range(3)}
print(dict)

