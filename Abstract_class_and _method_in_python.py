'''
Python by default cannot support abstract class and method, but we have a module called abc(abstract base classes) module 
you can use here to achieve abstract class
Abstract classes are classes that contain one or more abstract methods.
 An abstract method is a method that is declared, but contains no implementation. 
 Abstract classes cannot be instantiated, require subclasses to provide implementations for the abstract methods.
'''

from abc import ABC, abstractclassmethod    


class computer(ABC):

    # The method only has declaration but don't have definition. we call it absract method
    @abstractclassmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("it's running")

class whiteboard(computer):
    def write(self):
        print("it's writing")

class programmer:
    def work(self,com):
        print("Sovling Bugs")
        com.process()
#com = computer()
com1 = laptop()
#com.process()

com1 = laptop()
'''
Subclasses derived from a specific abstract base class must implement the methods and properties provided in that abstract base class. 
Otherwise, an error is raised during the object instantiation.
'''
 # com2 = whiteboard() This subclass doesn't implement the methods and properties provided in that abstract base class.
 # so it cannot work 

prog1 = programmer()
prog1.work(com1)











print()
print("---------------------------------------------------")
print()



class AbstractClass:
    
    def do_something(self):
        pass
    
    
class B(AbstractClass):
    pass

a = AbstractClass()
b = B()

'''
If we start this program, we see that this is not an abstract class, because:
we can instantiate an instance from
we are not required to implement do_something in the class defintition of B
'''
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractclassmethod
    def do_something(self):
        pass
'''
class DoAdd42(AbstractClassExample):
    pass

x = DoAdd42(4)
----------------------------------------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-2bcc42ab0b46> in <module>
      2     pass
      3 
----> 4 x = DoAdd42(4)

TypeError: Can't instantiate abstract class DoAdd42 with abstract methods do_something
-----------------------------------------------------------------------------------------------------------

'''



class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42
    
class DoMul42(AbstractClassExample):
   
    def do_something(self):
        return self.value * 42
    
x = DoAdd42(10)
y = DoMul42(10)

print(x.do_something())
print(y.do_something())


#A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.



'''
You may think that abstract methods can't be implemented in the abstract base class. This impression is wrong: 
abstract method can have an implementation in the abstract class!
Even if they are implemented, designers of subclasses will be forced to override the implementation. 
Like in other cases of "normal" inheritance, the abstract method can be invoked with super() call mechanism. 
This enables providing some basic functionality in the abstract method, which can be enriched by the subclass implementation.
'''


 
class AbstractClassExample(ABC):
    
    @abstractclassmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()