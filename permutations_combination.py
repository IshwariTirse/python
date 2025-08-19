# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 09:48:01 2025

@author: ADMIN
"""

#combination
from itertools import combinations
players=["Jay","jani","janardhan","ishu"]
for i in combinations (players,2):
    print(i)
    
from itertools import combinations
players=['ishu','rutu','dyanu','vaishu']
for j in combinations(players,2):
    print(j)
    
    

#permutations used when ordering or arranging items 
from itertools import permutations
players=["John","Jani","Janardhan"]
for seat in permutations(players,2):
    print(seat)
    

#product is used when you will having 2 list
#and possibly arrangements
from itertools import product
team_a=["Rohit","Pandya","Bumrah"]
team_b=["virat","manish","sami"]
for pair in product(team_a,team_b):
    print(pair)
    
#shallow copy and deep copy
list_a=[1,2,3,4,5]
list_b=list_a
print("ID of old List",id(list_a))
print("Id of new list",id(list_b))
list_a[0]=-10
print(list_a)
print(list_b)

#shallow 

def get_pin(input):
    words=input.split()
    total_length=sum(len(word) for word in words)
    while total_length>=10:
        total_length=sum(int(digit) for digit in str(total_length))
    return total_length
get_pin("the good the bad and the ugly")
get_pin("Wipro Technologies")
        
