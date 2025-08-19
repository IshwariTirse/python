# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 09:18:31 2025

@author: ADMIN
"""
input1=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
def sum_of_odd(input1):
    current_length=0
    current_sum=0
    max_length=0
    longest_sum=[]
    for num in input1:
        if num%2!=0:
            current_length+=1
            current_sum+=num
        else:
            if current_length>max_length:
                max_length=current_length
                longest_sum=[current_sum]
            elif current_length==max_length:
                longest_sum.append(current_sum)
            current_length=0
            current_sum=0
    if current_length>max_length:
        max_length=current_length
        longest_sum=[current_sum]
    else:
        current_length==max_length
        longest_sum.append(current_sum)
    print(sum(longest_sum)if longest_sum else -1)
input1=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
sum_of_odd(input1)
input1=[1,3,5,2,7,9,11,4,13,15,17]
sum_of_odd(input1) #81 wrong output
input1=[1,3,5,7,9]
sum_of_odd(input1)
input1=[]
sum_of_odd(input1) # 0 wrong output
input1=[7]
sum_of_odd(input1)
input1=[2,5,4,7,6,3]
sum_of_odd(input1) #15 wrong output
input1=[2,4,6,8]
sum_of_odd(input1) #0 wrong output expected -1
input1=[1,3,5,7,9]
sum_of_odd(input1) 
input1=[1,3,0,5,7,0,9,11]
sum_of_odd(input1) #wrong output 36 expected 4



"""
sum of power of digits
example if the given number is 582109 the sum of powers 
of digits==(5 raised to the power of 8)+(8 raised to the power)
=390625+64+2+1+0+1=390693
input1 represent the given number
the function is expected to return the 
sum of powers of digits of input1
"""
def sumofpowerofdigits(input1):
    num_str=str(input1) #convert no to string
    total_sum=0
    for i in range(len(num_str)):
        base=int(num_str[i])
        if i+1 < len(num_str):
            exponent=int(num_str[i+1])
        else:
            exponent=0
        total_sum+=base**exponent
    return total_sum
test_number=582109
print(sumofpowerofdigits(test_number))      

input1=50
print(sumofpowerofdigits(input1))

input1=7
print(sumofpowerofdigits(input1))

input1=204 #2
print(sumofpowerofdigits(input1))

input1=1111 #4
print(sumofpowerofdigits(input1))

input1=987 #45143874
print(sumofpowerofdigits(input1))

input1=105 #2
print(sumofpowerofdigits(input1))

input1=1000 #4
print(sumofpowerofdigits(input1))

input1=98 #43046722
print(sumofpowerofdigits(input1))

def sum_of_power_of_digits(n):
    s = str(n)
    total = 0
    for i in range(len(s)):
        base = int(s[i])
        exponent = int(s[i+1]) if i+1 < len(s) else 0
        total += base ** exponent
    return total

# Example usage:
print(sum_of_power_of_digits(582109))  # → 390693

def sum_digits(n):
    s=str(n)
    total=0
    for i in range(len(s)):
        base=int(s[i])
        exponent=int(s[i+1]) if i+1<len(s) else 0
        total+=base**exponent
    return total
print(sum_digits(582109))
                   
def sum_digits(n):
    s=str(n)
    total=0
    for i in range(len(s)):
        base=int(s[i])
        exponent=int(s[i+1]) if i+1<len(s) else 0
        total+=base**exponent
    return total
print(sum_digits(582109))
print(sum_digits(50))
print(sum_digits(7))    
print(sum_digits(1111)) #4
print(sum_digits(204))  #2
print(sum_digits(987)) #45143874
print(sum_digits(105))  #2