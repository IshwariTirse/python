# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 18:19:11 2025

@author: ADMIN
"""
def plindrome(in1):
    if in1=="":
        return "you entered wrong input"
    else:
        str=in1[::-1]
        if str==in1:
            return True
    return False
print(plindrome("madam"))

no1,no2=0,1
n=int(input("enter value of n"))
for i in range(n):
    print(no1)
    result=no1+no2
    no1=no2
    no2=result
        
    
    
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter value of n: "))
for i in range(n):
    print(fibonacci(i))

lst = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)
#[1, 2]
l=[1,2,4,5,3,4,5,9,0]
duli=[]
for i in l:
    if l.count(i) > 1 and i not in duli:
        duli.append(i)
print(duli)
#[4, 5]

#check if two strings are anagram
def are_arguments(str1,str2):
    return sorted(str1)==sorted(str2)
print(are_arguments("listen","silent"))

#move all zeros at the end of list       
def move_zero(lst):
    non_zero=[x for x in lst if x!=0]
    return non_zero+[0]*(len(lst)-len(non_zero))
print(move_zero([0,1,0,3,12]))
#[1, 3, 12, 0, 0]
#count pairs with given sum in a list
def count_pairs(lst,target):
    count=0
    seen=set()
    for num in lst:
        if target-num in seen:
            count+=1
        seen.add(num)
    return count
print(count_pairs([1,5,7,-1,5],6))
#3
#find if a number is a strong number
def is_strong(num):
    def factorial(n):
        return 1 if n==0 else n * factorial(n-1)
    return num==sum(factorial(int(d)) for d in str(num))
print(is_strong(145))
is_strong(2)
is_strong(123)

#find the first non repeating character in a string
def first_unique_char(s):
    for ch in s:
        if s.count(ch)==1:
            return ch
        return None
print(first_unique_char("engineering"))#None
first_unique_char("leetcode")#l
first_unique_char("Saathi")#S