'''
polymorphism -> One thing can take many form. Like human, we have different form, as environment change, 
we have different behavior
In the same way, object has multiple form. This concept is very important in loose coupling
dependency injection, interface
The are four ways of implementing polymorphism 
1. Duck typing
2. Operator overloading 
3. method overloading
4. method overriding 
'''

'''Duck typing
we use different behavior to describe an object.
Therefore, once some object conform to some behaviors, we would think that it might belong to specified class

Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important 
than the methods it defines. When you use duck typing, you don't check types at all. Instead, you check for
the presence of a given method or attribute
We don't care certian type of object. we only care if it can do what we ask 
'''

class pycharm:
    
    def excecute(self):
        print("Compiling") 
        print("Running")


class editor:
    def excecute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")


class laptop:
    def code(self, ide):
        ide.excecute() 


ide = editor()
ide2 = pycharm()
lap1 = laptop()
lap1.code(ide)
print("-----------------------------------------------------")
lap1.code(ide2)