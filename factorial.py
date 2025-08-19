# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 09:02:33 2025

@author: ADMIN
"""
#factorial of a number
def factorial(z):
    if z==1:
        return 1
    else:
        return(z*factorial(z-1))
factorial(3)
factorial(6)

#lambda function
def add(a):
    sum=a+10
    return sum
add=lambda a:a+10
print(add(20))

add=lambda a,b:a+10
print(add(5,6))

#map function
lst=[22,11,44,55,66]
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)

lst=[34,12,64,55,13,76]
odd_lst=list(filter(lambda x:(x%2==0),lst))
print(odd_lst)

import math
def min_cost(no_banana,lot1,price1,lot2,price2):
    lot_a=math.ceil(no_banana/lot1)
    lot_b=math.ceil(no_banana/lot2)
    print(f"lot_a(vendor1):{lot_a} to cover {no_banana} bananas")
    print(f"lot_b(vendor2):{lot_b} to cover {no_banana} bananas")
    #Total cost for each vendor
    cost_a=lot_a*price1
    cost_b=lot_b*price2
    print(f"cost_a(vendor1):{cost_a}")
    print(f"cost_b(vendor2):{cost_b}")
    return min(cost_a,cost_b)
#test case5
min_cost(1000,50,400,40,350)

