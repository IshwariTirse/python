# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 15:42:24 2025

@author: ADMIN
"""
d={
   "bank":"HDFC",
   "address":"kopargaon",
   "pincode":423604,
   "cust_id":10230
   }
print(d)
d.pop("cust_id")
print(d)
d.clear()
print(d)


f={
   "money":900000,
   "cash":"yes",
   "happy":"yes"
   }
print(f)

books={
       "biography":{
           "name":"Ishu",
           "author":"Ishwari_Tirse",
           "date":"07-03-1999",
           "hit":"yes"
       },
       "biography2":{
           "name":"AC_to_IAS",
           "author":"sasa",
           "post":"IAS"
           }
}
print(books)

"""
An event planner needs to rent at least total_chairs chairs for a wedding.

Rental Company X offers packages of pkg1 chairs for cost1.

Rental Company Y offers packages of pkg2 chairs for cost2.

Only full packages can be rented from one company. Write a function to find the cheapest rental cost.

python
Copy
Edit
"""
import math
def event(total_chairs,pkg1,cost1,pkg2,cost2):
    pakages_x=math.ceil(total_chairs/pkg1)
    pakages_y=math.ceil(total_chairs/pkg2)
    print("package x is",pakages_x)
    print("pakages y is",pakages_y)
    cost_x=pkg1*cost1
    cost_y=pkg2*cost2
    print("cost_x",cost_x)
    print("cost_y",cost_y)
    print(min(cost_x,cost_y))
event(100,9000,10,800,80)

y={'ishu','rutu','rani'}
a=0
dict1=dict.fromkeys(y,a)
print(dict1)
'''
 package x is 1
 pakages y is 1
 cost_x 90000
 cost_y 64000
 64000
 {'rutu': 0, 'ishu': 0, 'rani': 0}
 '''

