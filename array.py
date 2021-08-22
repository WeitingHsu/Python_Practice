from array import *
# import all the function in array
import matplotlib as plt
import pandas as pd
#print("Hello world")

#firstname = input("Enter your first name")
#lastname = input("Enter your last name")

#print("Your whole name is ",firstname, lastname)

vals = array('i',[5,9,-8,4,2])
vals.append(1)

new_arr = array(vals.typecode,(a*a for a in vals))
print(new_arr)

for i in range(len(vals)):
    print(vals[i])

# split function 
''' 
name = input("Please input your value")
firstname = name.split()[0]
lastname = name.split()[1]

print("Last name is "+lastname)
print("First name is "+firstname)
'''

# append function

arr = array('i',[])

n = int(input("Enter length of array"))

for i in range(n):
    arr.append(int(input("Please enter next value")))

print(arr)

print(type(arr))
print(type(1))

# index function

print(arr.index(arr[0]))
