'''
An iterator is an object that can be iterated (looped) upon. 
It is used to abstract a container of data to make it behave like an iterable object. 
You probably already use a few iterable objects every day: strings, lists, and dictionaries to name a few.

An iterator is defined by a class that implements the Iterator Protocol. 
This protocol looks for two methods within the class: __iter__ and __next__.

Whoa, step back. Why would you even want to make iterators?

Saving memory space
Iterators don’t compute the value of each item when instantiated. 
They only compute it when you ask for it.
 This is known as lazy evaluation.

Lazy evaluation is useful when you have a very large data set to compute. 
It allows you to start using the data immediately, while the whole data set is being computed.



'''



nums = [7,8,9,5]

for i in nums:
    print(i)
print()
print("-----------------------------------")
print()

it = iter(nums)
print(it.__next__())
print(it.__next__())

print(next(it))

print("---------------------------------------------------------------------")

class topten:

    def __init__(self):
        self.num = 1


    

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <=10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = topten()
print(type(values))
print(next(values))
print("--------------------------------")

for i in values:
    print(i)


