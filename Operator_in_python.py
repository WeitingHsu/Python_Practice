'''
Operator in python can be divied into 5 operators
1.Arithmetic operator
2.Assignment operator
3.Logical(bitwise) operator
4.Unary(Identity ) operator  
5. Comparison(Relational) operator
'''


'''  Arithmetic operator '''
print("Arithmetic operator")

# No a=*2 or a=+2

# Modulus
b = 10%3
# Exponential
c = 2**5
# floor division
d = 5//2

print([b,c,d])


'''  Assignment operator '''
print("Assignment operator")
a = 10
a+=2
print(a)
a*=10
print(a)

a,b,c,d = 1,2,3,4
print([a,b,c,d])

'''  Unary operator '''
print("Unary operator")
a = 1
b = 2
c = a is b
d = a is not b
print(c,d)
n = 7
n = -n
print(n)


''' Logic operator '''
print("Logic operator")
a = True
b = False
c = a & b
d = a | b
e = not a
f = not (a & b)
g = not (a | b)

print("1&0 = ",c,";1|0 = ",d,";not 1 = ",e,";not (1&0) = ",f,";not (1|0)=",g,";~1=",~1,";~0=",~0,";~2=",~2,";~3=",~3)
print(~True)

# XOR
h1 = 1^0
h2 = 0^1
h3 = 0^0
h4 = 1^1

# Bit operation
h5 = 3^2 #(11^10 = 01 = 1)
h6 = 3^4 #(11^100 = 111 = 7)
h7 = 5&2 #(101&10 = 000 = 0)

print("1^0=",h1,";0^1 = ",h2,";0^0 = ",h3,";0^0 = ",h4,";3^2 = ",h5,";3^4 =",h6,";5&2 = ",h7)

# x << y (logic shift operation)
'''
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
This is the same as multiplying x by 2**y.
'''
i1 = 8<<1 # 1000 shit left by 1 = 10000 = 16(dec) 
# x >> y  (logic shift operation)
'''
Returns x with the bits shifted to the right by y places. 
This is the same as //'ing x by 2**y.
'''
i2 = 2>>1 # 10 shift right by 1 = 01 = 1(dec)


print("8<<1 =",i1,"2>>1 =",i2)

'''  Comparison operator '''
print("Comparison operator")

print("1>2=",1>2,"1==2 = ",1==2,"1!=2=",1!=2)


''' Numeric conversion '''

print("bin(35)=",bin(35))
print("hex(35)=",hex(35))
print("oct(35)=",oct(35))
print("0b10100010",0b10100010)
print("0x3243abc",0x3243abc)
print("0o345234",0o345234)

print(~(-3))
print(-(~3))