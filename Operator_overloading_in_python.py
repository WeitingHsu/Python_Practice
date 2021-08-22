'''Operator overloading
In python, self-define object can't use default object method(function) like plus, minus, multiplication...
Therefore, to overcome it, we should cite default or other object's method to create the same method but can't be 
used in our object. This is called operator overloadding. 
The reason it call operator overloading is because normally we use on operator to extend the limit 
on operator usage. 
'''


a = 5
b = 6
c ='s'
d = 't'

print(5+6)

print(int.__add__(a,b))
print(str.__add__(c,d))


class student:

    def __init__(self,m1,m2,m3,m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
    # create the same name method(function) as other object's method like int, float,....
    # Same method but with different type argument(object)
    def __add__(self,other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        m3 = self.m3+other.m3
        m4 = self.m4+other.m4
        s3 = student(m1,m2,m3,m4)
        return s3

    def __gt__(self,other):
        selfsum = self.m1+self.m2+self.m3+self.m4
        othersum = other.m1+other.m2+other.m3+other.m4
        if selfsum>othersum:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} {} {}'.format(self.m1,self.m2,self.m3,self.m4)



s1 = student(54,85,76,96)
s2 = student(32,64,85,90)

s3 = s1+s2

print(s3.m1)

sgt = s1>s2
print(sgt)

print(s1)
print(s2)

# we can directly plus two object together. X -> s3 = s1+s2