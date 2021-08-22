class computer:
    
    # __init__ can be regarded as intial setting with it. Every object should have these attribute
    # self is directly point to object itself. every object should have different have same attribute 
    # but with different content inside it

    def __init__(self,cpu,ram):
        self.cpu = cpu         # if you don't do default setting in class template, 
        self.ram = ram         # you should specify value for it before using it. Otherwise, it will require 
                               # you to give these two argument. 
        self.name = "Weitng"   # These are default setting in every object
        self.age = 25          # Variable inside __init__ is instance variable

    def config(self):
        print("config is ",self.cpu,self.ram)

    def update(self):
        self.name = "Kevin"
        self.age = "28"
    def compare(self,other):
        if self.age ==other.age:
            print(self.name,"has the same age with",other.name)
        else:
            print(self.name,"is not as old as",other.name)

com1 = computer('i5',16)
com2 = computer('Ryzen 3',32)

com1.config()
com2.config()

com1.name = "Willy"
com2.update()

print(com1.name)
print(com2.name)

com1.compare(com2)


print(id(com1))
print(id(com2))

# Size of object depends on the number of variables and size of each variable 
# constructor used to allocate size to object



print("-------------------------------------------------------------------------------")
'''        Types of variable                          '''

# Namespace is an area where you create and store object/variable
# Class namespace
# Object/Instance namespace

class car:
    # class variable is used for every object. every object should have the same feature
    # class variable can also be regarded as static variable in C++
    wheels = 4

    # Instance variable is used for specifying different feature for different object
    # Instance variable can also be regarded as dynamic variable in C++
    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = car()
c2 = car()

c1.mil = 20
c2.mil = 30

car.wheels = 2  # The momoent you change this, it affect all the object, becasue it's modifying the template(class)


print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)

