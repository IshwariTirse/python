# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 17:52:56 2025

@author: ADMIN
"""

#program to find longest odd series
input1=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
max_seq = []
current_seq = []
for num in input1:
    if num % 2 != 0:
        current_seq.append(num)
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
    else:
        current_seq = []
print("Longest odd sequence:", max_seq)
#Longest odd sequence: [13, 15, 17, 19]

inp=[3,1,5,2,4,7,9,11,8,10,12,13,15,17,19]
max_seq=[]
current_seq=[]
for num in inp:
    if num%2!=0:
        current_seq.append(num)
        if len(current_seq)>len(max_seq):
            max_seq=current_seq
    else:
        current_seq=[]
print("maximum odd sequence",max_seq)
#maximum odd sequence [13, 15, 17, 19]

input=[3,1,5,2,4,7,9,11,13,15,17,19]
max_seq=[]
current_seq=[]
for num in input:
    if num%2!=0:
        current_seq.append(num)
        if len(current_seq)>len(max_seq):
            max_seq=current_seq
    else:
        current_seq=[]
print("the longest odd sequence is",max_seq)
#13, 15, 17, 19]


