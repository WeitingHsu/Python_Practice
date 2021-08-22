

def add_sub(x,y):
    add = x+y
    sub = x-y
    return add,sub
result1,result2 = add_sub(9,2)

print(result1, result2)

'''In Python, we don't have the concept of 'pass by value' or 'pass by reference'. 
Instead, we have immutable or mutable arguments passed to the function.
 If we pass immutable objects like integer or string to function and try to update their value, 
 their original value will not be updated 
 instead a new variable will be created with updated value at new memory address.
  If we pass mutable objects like list or dictionary and try to update them, 
  their original value will be updated at the same memory address.'''


def update1(x):
    print("address after pass to function:",id(x))
    x = 8
    print("address after x is assigned new value: ",id(x))


def update2(lst):
    print("address after pass to function:",id(lst))
    lst[1] = 8
    print("address after lst is assigned new value in the list: ",id(lst))
    print("lst",lst)

a = 10
print("address before any function operation:",id(a))
update1(a)
print("address after function operation:",id(a))

lst = [10,12,15]
print("address before any function operation:",id(lst))
update2(lst)
print("address after function operation:",id(lst))



def person1(name,age):
    print(name)
    print(age)

# default setting for function
def person2(name,age = 28):
    print(name)
    print(age)


person1(28,"Kelvin")
# arguement assignment for function so that it won't assign wrong even if argument placement is wrong
person1(age = 28,name = "Kelvin")

#  *b means it could be a multiple value(If it is, it means it is tuple data type)
def sum(a,*b):
    print(type(b))
    c = a
    for i in b:
        c = c+i

    print(c)

sum(5,6,7,8)


# multiple unknown assigned arguement; **data is a dictionary

def person3(name,**data):
    print(type(data))
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)



person3('navin',age = 28, city = 'Mumbai',mob =984783)


''' Global variable vs Local variable '''

# g as a global variable, can be accessed even in function
g = 10
a = 5
print("id a", id(a))



def sth1():
    b = 10
    # b is local variable which can only be accessed in function, but can't be accessed outside the function
    print(g)
    # if we declare variable as global insie function, it means this varaible can also  be accessed outside function
    global c
    c = 10
    print("global inside function c",c)
    # if we want to create local varaible a, but still want to access global variable. How do we achieve this
    # It comes to using globals function to get the global data address as 
    # globals()[global variable you want in bunches of global variables ]

    a = 9
    x = globals()['a']
    print("x",x)
    print("id x",id(x))
    print("id5",id(5))


def sth2():
    print("global in different function c",c)

sth1()
sth2()

print("global outside function c",c)

# pass list inside function

def odd_even(lst):

    even =0
    odd =0

    for i in lst:
        if i%2 !=0:
            odd+=1
        else:
            even+=1
    return even, odd

lst = [1,23,243,63,6,234,65,23,7,6,3211,128,67]

even, odd = odd_even(lst)

print("Even amount {}, and odd amount {}".format(even,odd))



'''  Anonymous function  '''

f = lambda a,b:a*b


result = f(5,6)

print(result)

'''
def is_even(n):
    return n%2==0
'''
nums = [3,2,6,4,6,32,54,23,12,53,65,75]




'''
filter(function or None, iterable) --> filter object
Return an iterator yielding those items of iterable for which function(item) is true.
If function is None, return the items that are true.
Note: it doesn't return expression result, but a iterator
'''

is_even = lambda n:n%2==0
evens = list(filter(is_even,nums))

'''
map(func, *iterables) --> map object
Make an iterator that computes the function using arguments from each of the iterables.
Stops when the shortest iterable is exhausted.
'''

doubles = list(map(lambda n:n*2,nums))

'''
reduce(function, sequence[, initial]) -> value
Apply a function of two arguments cumulatively to the items of a sequence, from left to right, 
so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
If initial is present, it is placed before the items of the sequence in the calculation, 
and serves as a default when the sequence is empty.
'''
from functools import reduce
sum = reduce(lambda a,b:a+b,doubles)


print(evens)
print(doubles)
print(sum)