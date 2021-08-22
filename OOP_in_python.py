'''
Object-oriented programming is a very important feature in python. 
Besides OOP, python also can use functional programming and prpcedure programming. 
That's the reason why python is so popular nowadays.
In OOP, every object has its own attribute(data) and behavior(algorithm,function)
Therefore, when think about big project, try to establish different small objects and connect it together
when applying OOP, you have to design a template(class) first, and then you can utilize this template 
to create different object.
In summary, class is a design(template), and obejct is an instance.
'''

class Computer:

# self is object you are boxing
    def config(self):
        print("i5, 16gb, 1TB")


com1 = Computer()
com2 = Computer()

print(type(com1))

Computer.config(com1)
Computer.config(com2)


# Normally used the following method on object
com1.config()  # Behind the scene, the config takes com1 as argument 
com2.config()

a = 8
print(a.bit_length())
