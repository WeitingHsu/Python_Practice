'''
Recall that generator functions allow us to create iterators in a more simple fashion.

Generators introduce the yield statement to Python. 
It works a bit like return because it returns a value.

The difference is that it saves the state of the function. 
The next time the function is called, execution continues from where it left off,
with the same variable values it had before yielding.
'''


def topten():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
values = topten()

print(values)
print(values.__next__())

print("------------------------")
for i in values:
    print(i)


def top():
    n =1
    while n<=10:
        yield n*n
        n+=1

val = top()

for i in val:
    print(i)

print(2**0.5)