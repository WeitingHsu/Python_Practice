# list use [] to include all the element to form a list
# different data type can be put together inside list
# list index is like array

nums = [12,34,5,23,65,32,21]

mix1 = ['das',23,8.5]

tup = (2,3,4)
set = {21,32,53,53}

mix2 = [12,'3232',tup,set,mix1]


print(mix2[2][2])
print(mix2[3])   # set cannot be indexed
print(mix2[4])

print(mix2[4][1])

# insert value to assigned index
mix2.insert(2,2)

print(mix2)

# remove assigned index value
mix2.pop(2)
print(mix2)
# if you don't specify index for pop, it will directly remove last element out
mix2.pop()
print(mix2)

# The way you delete multiple value 
del mix2[2:]
print(mix2)

# The way to add multiple value inside list
mix2.extend([29,(23,24),'232',{3,4,4}])
print(mix2)


print(min(nums))
print(sum(nums))

# arrange order of number from small to big in the list
nums.sort()
print(nums)