# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 09:10:01 2025

@author: ADMIN
"""
in1=[11,3,1,4,7,8,12,2,3,7]
def count_decreasing_sequence(in1):
    in2=len(in1)
    count_se=0
    max_len=0
    curr_len=1

    for i in range(1, in2):
        if in1[i]<in1[i-1]:
           curr_len+=1
        else:
            if curr_len>1:
               count_se+=1
               max_len=max(max_len,curr_len)
        curr_len=1
            
    if curr_len>1:
        count_se+=1
        max_len=max(max_len,curr_len)
    return count_se,max_len
#print("total decreasing seq",count_se)
#print("longest decreasing sequence length",max_len)
"""
print(count_decreasing_sequence([11,3,1,4,7,8,12,2,3,7]))
print(count_decreasing_sequence([1,2,3,4]))
print(count_decreasing_sequence(input))
print(count_decreasing_sequence(100))
print(count_decreasing_sequence([]))
print(count_decreasing_sequence([5]))
print(count_decreasing_sequence(4,4,4,4))
print(count_decreasing_sequence(9,8,7,6,5))
print(count_decreasing_sequence(1,2,3,4,5))
print(count_decreasing_sequence(7,5,6,4,5,3))
"""
print(count_decreasing_sequence([11, 3, 1, 4, 7, 8, 12, 2, 3, 7]))
print(count_decreasing_sequence([1, 2, 3, 4]))
print(count_decreasing_sequence([100]))                   
print(count_decreasing_sequence([]))                      
print(count_decreasing_sequence([5]))
print(count_decreasing_sequence([4, 4, 4, 4]))
print(count_decreasing_sequence([9, 8, 7, 6, 5]))
print(count_decreasing_sequence([1, 2, 3, 4, 5]))
print(count_decreasing_sequence([7, 5, 6, 4, 5, 3]))



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

#sum_of_odd(input1)

