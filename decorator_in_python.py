'''
Decorator is used for modifying the function without changing its orignal module
Imagine a situation. you are import a function or module that you can't modify
But you don't wanna duplicate the fucntion and add something to that. How do you do in this situaiton?
It comes to decorator
'''
# The following function is not with you, you can't modify it
def div(a,b):
    print(a/b)


# write a function inside a funciton
# input will be the function you want to modify
def smart_div(func):
    # This inside function is taking the same parameter of which you are going to modify. 
    # It's redesing the function you want
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner


div = smart_div(div)


div (2,4)