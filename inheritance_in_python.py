'''
Inheritance talk about parent class and child class
child class inherit all the method and attribute the parent has 



'''



class A:
    def feature1(self):
        print("Featur 1 working")
    
    def feature2(self):
        print("Feature 2 working")

# inheritance example : A is super class. B is sub class.Single level inheritance 
class B(A):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
# multi-level inheritance
class C(B):
    def feature5(self):
        print("Featur 5 working")


class D:
    def feature6(self):
        print("Featur 6 working")

# Multiple inheritance
class E(A,D):
    def feature7(self):
        print("Featur 7 working")

a1 = A()
a1.feature1()

b1 = B()
b1.feature1()
b1.feature2()

c1= C()
c1.feature1()
c1.feature3()
c1.feature5()

e1 = E()
e1.feature1()
e1.feature6()