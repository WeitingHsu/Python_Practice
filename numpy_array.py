from numpy import *

'''


# In array, all the element should be the same type.


# it should be the same type, so it convert other element to float.
arr = array([1,2,3,4,5.0])
print(arr.dtype)
print(arr)

# directly convert it to float
arr1 = array([1,2,3,4,5],float)
print(arr1.dtype)
print(arr1)

# linspace  create linear space of array
arr2 = linspace(0,15,16)
print(arr2)

# logspace  create log space of array
arr3 = logspace(0,10,5)
print(arr3)

# arange create specified interval of array
arr4 = arange(1,15,2)
print(arr4)

# 
arr5 = array([1,2,3,4,5])
arr6 = array([1,2,3,4,5])
arr5 = arr5 + 5
arr7 = arr5+arr6
print(arr5)
print(arr7)

# lots of function to use

print("mean value of array5 is",mean(arr5))
print("max value of array5 is",max(arr5))
print("min value of array5 is",min(arr5))
print("sqrt value of array5 is",sqrt(arr5))
print("log10 value of array5 is",log10(arr5))
print("sum value of array5 is",sum(arr5))
print("concatenate value of array5 and arr6 is",[arr5,arr6])


# Difference between copy(deep copy) and view(shallow copy)

arr7 = arr5
arr8 = arr5.view()
arr9 = arr5.copy()

arr5[1] = 9

print(arr5)
print(arr7)
print(arr8)
print(arr9)
# arr9 doesn't change value of second element
# shallow copy link two variable, but deep copy doesn't

print(id(arr5)) # id is address of variable
print(id(arr7))
print(id(arr8))
print(id(arr9))

# arr5 and arr7 have the same address, but arr8.

'''

'''                     two dimensional array           '''

arr1 = array([
    [1,2,3,6,2,9],
    [4,5,6,7,5,4],
])

arr2 = arr1.flatten()

arr3 = arr1.reshape(2,2,3)

print(arr1.dtype)
print(arr1.shape)
print(arr1)
print(arr2)
print(arr3)
print("----------------------------------")

# convert array to matrix (matrix can be seen as small set of array, which can be applied with mathematical operation)
m1 = matrix(arr1)
print(m1)
# the matrix formation is the same as array, but it can perform mathematical operation
# anotehr way to create matrix
m2 = matrix('1,2,3;4,5,6;7,8,9')
m3 = matrix('1,2,3;4,5,6;7,8,9')
print(m2) 
print(diag(m2))
print(m2.max())

m4 = m2*m3
print(m4)

