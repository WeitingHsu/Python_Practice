''' In this example, class inside class is introduced
You can create object of inner class inside the outer class or
you can create object of inner class outside the outer class
provided you use outer name to call it



'''



class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno  = rollno
        # Important statement for outer class to point to inner class
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)

    # inner class created inside outer class. it also can be seen as an attribute of outer class
    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu)

stu1 = student('Weiting',2)
stu2 = student('Willy',4)

lap1 = stu1.lap
lap2 = stu2.lap

print(id(lap1))
print(id(lap2))

lap1.show()