# equation in tuple is faster than list
# tuple is like list but can't be changed

tup = (1,2,3,4)
print(tup[1])
print(type(tup))

# set is a set but don't have a particular direction or say it has random order
# Even if you set has repeated value, it will discard redundant repeated value
# index is also not supported in set due to no specific order for set.
# s is like list, but doesn't have order and support duplicate value
s = {22,34,52,12}
s1 = {98,98,23,98,23,8,54,24,5}
print(type(s))
print(s)
print(s1)
s.add(1)
print(s)



