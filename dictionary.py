# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s={
   "book":"XML",
   "id":123
   }
s.pop("book")
print(s)
#{'id': 123}
s.clear()
print(s)
#{}

thisdic={
        "book":"XML",
        "id":123
        }
dic1=dict(thisdic)
print(dic1)
#'book': 'XML', 'id': 123}

#nested dictionary
our_family={
    "child":{
        "name":"manoj",
        "age":29,
        "post":"AC"
        },
    "child1":{
        "name":"adesh",
        "age":20
        }
    }
our_family


x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict





#get() to get the value of dictionary
car={
     "brand":"ford",
     "model":"Mustang",
     "year":1964
     }
car.items()
car.values()
car.update({"brand":"maruti"})
car

family={
        "father":"Bhaskar",
        "Mother":"Vanita",
        "daughter":"Ishu",
        "son":"Nilu"
        }
family.items()
family.values()
family.update({"daughter":"Ishwari"})
print(family)
#sort dict by key
data={'b':2,'a':5,'c':1}
data.items()
sorted_by_keys=dict(sorted(data.items()))
print(sorted_by_keys) 


r={"a":9,"b":6,"c":3,"d":4,"e":1,"f":10}
r.items()
s_by_key=dict(sorted(r.items()))
print(s_by_key)
                    
def add(a):
    sum=a+10
    return sum
add(20)

add=lambda a:a+10
print(add(20))


#sort by value
data={'b':2,'a':5,'c':1}
sorted_by_values=dict(sorted(data.items(),key=lambda item:item[1]))
print(sorted_by_values)




fruit_dict={"mango":200,"apple":100,"grapes":350,"banana":120}
sorted_by_values=dict(sorted(fruit_dict.items(),key=lambda item:item[1]))
print(sorted_by_values)
fruit_key=min(fruit_dict,key=fruit_dict.get)
#fruit_key=min(fruit_dict)
fruit_value=fruit_dict[fruit_key]
print(f"you will get the lowest priced items {fruit_key} {fruit_value} for free")
   
      
   
#sorting in descending order
sorted_by_values_desc=dict(sorted(sorted_by_values.items(),key=lambda item:item[1], reverse=True))
print(sorted_by_values_desc)

#adding val.ues to dictionary
dict1={'apple':'100','grapes':'120','mango':'200'}
sum=0
for value in dict1.values():
    sum=sum+int(value)
print(sum)

dict1={'apple':'100','grapes':'120','mango':'200'}
total_sum=sum(int(value)for value in dict1.values())
print(total_sum)

#concsatenation of dictionary
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
print(dict1)
dict1=dict1|dict2
print(dict1)

x={"a":0,"b":9,"t":8}
y={"w":5,"q":2,"o":1}
z={"c":80,"l":67,"k":23}
z.update(x)
print(z)
#write a program to check if a given key is already exist
dict1={'a':20,'b':30}
print('a'in dict1)

c={'abc':450,"xyz":120}
print('abc' in c)
i=1
while i<6:
    print(i)
    if(i==3):
        break
    i=i+1
   
i=1
while i<6:
    print(i)
    if(i==3):
        continue
    i+=1
    
#simple function
def my_fun():
    print("hello ishwari")
my_fun()
     
#function with argument
def my_fun(name):
    print("hello"," " +name)
my_fun("ishu")


def f(ag):
    print("hii" " "+ag)
f("ishu")

#function with positional argument
def my_fun(name,name1):
    print(name+" "+name1)
my_fun("helloo","world")
my_fun("world","hello")


def s(lover1,lover2):
    print(lover1+" "+lover2)
s("Manoj","ishwari")
#fun with arbitrary arguments, *args
#if you dont know how many arguments
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("Tappu","sonu","soni")

def r(*a):
    print(a[1]+" "+a[3])
r("sakshi","sujata","samruddhi","sanika")

#for key value in function use kwargs
def myfun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
myfun(first_name='popalal',mid_name='mohanlal',last_name='goyal')
"""
**kwargs collects all keyword arguments into a dictionary.
kwargs.items() returns a list of (key, value) tuples from that dictionary.
The for loop iterates through these items and prints each key-value pair in the format key:value.

"""

def my_function(country="norway"):
    print("i am from"+country)
my_function("india")
my_function("brazil")
my_function("london")
my_function()


def college(name="sanjivani"):
    print("i am from"+name)
college("amrutvahini")
college("Pravara")
college("MIT")
college("Matoshri")
college("SND")
college()

fruits=["orange","banana","guava"]
def my_fun(fruits):
    for x in fruits:
        print(x)


#function return a value
def my_fun(x):
    y=x*5
    return y
my_fun(5)

def r(x):
    a=x+2
    return a
r(0)

def my_function(x):
    y=x*5
    z=x*7
    return y,z
my_function(5)

def op(x,y):
    a=x*y
    b=x+y
    c=x/y
    d=x-y
    return a,b,c,d
op(4,2)
#pass function
def my_function():
    pass
my_function()

def pasw(v):
    #pass
    f=v-1
    return f
    pass
pasw(1)
