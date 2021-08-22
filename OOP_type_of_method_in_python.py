

class student:

    school = "NTUST"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def average(self):
        return (self.m1+self.m2+self.m3)/3


    # The following are class method used to define class template function. when this function is used, all the object will be updated!
    @classmethod
    def getschool(cls):
        return cls.school
    @classmethod
    def setschool(cls,newschool):
        cls.school = newschool
    @classmethod
    def info(cls):
        return cls.school

    def classname():
        print("This is student coding class")

stu1 = student(10,30,24)
stu2 = student(12,35,27)



print(stu1.average())
print(stu2.average())

school1 = student.getschool()
print(student.info())
student.setschool("NTU")

print(stu1.getschool())
print(stu2.getschool())

student.classname()