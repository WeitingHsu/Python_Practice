'''   Address in python
Class is a template, and object is any one of its derivation.
In python, every data is a object,and every object has its own address
Every varaible should point to a object, so once variable point to different object, it also change its address
This is to say, variable actually doesn't have a memory. Instead, object endow variable with the address  
'''

a = 10
print(id(10))
print(id(a))
a = 12
print(id(a))
b = 12
print(id(b))
print(id(12))
a = 12.5
print(id(a))
print(id(12.5))