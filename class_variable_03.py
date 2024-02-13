# All Types of variable 
x = 100                 # --> Gloabal Variable(outside of the class)
class Student:
    y = 200             # --> Static Variable(inside class but outside of constructor and methods)
    
    def __init__(self,x,y) :
        
        self.name = x   # --> Instance Variable(Non-Static variable)
        self.roll = y   # --> (declared with self and always declared inside constructor)
        a = 400         # --> Local variable(declared inside constructor and methods but without self)

    def method1(self):
        z = 300         # --> Local variable(declared inside constructor and methods but without self)
