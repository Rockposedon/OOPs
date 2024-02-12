# class, object and reeference variable
""" EXPLANATION of Class and Object

class  : It acts as blue print/plan/model/design for objects.
object : A physical existenence of a class is object. Every object has
         properties(data) and behaviour, properties are specified by variables
         behaviour can be specified by methods
--> class and object has one to many relation
--> To create object class must required

example 1 : Building plan:
            artichetect design an plan for building (That is class)
            builder implements that design into physical building (That is object)

example 2 : LED TV samsung Model A
            TV Model design is Class
            Each TV is Object

"""

""" Types of Variables(variables are properties of an object)
    1. Instance variables(Object level variables)
    2. Static variables(Class level variables)
    3. Local variables(Method level variables)

"""

""" Types of Methods(methods are actions of an object)
    1. Instance methods
    2. class methods
    3. static methods
"""

""" Reference Variable : It can be used to refere an object, by using rv we can invoke/access the functionality of object.
    For single object multiple reference variable can be maintained

"""

""" SYNTAX OF Class 

class name_of_class:
    '''doc string'''
    properties (variables)--> variables is notjing but properties of an object(like name,marks,rollno)

    actions    (methods)  --> every object can invoke some functionality and that 
                              is notjing but an methods that we define in class(like read,write,sleep,talk)
"""


class Student:

    '''This is nothing but doc string and we can print it using __doc__ and help(class_name)'''  
    def __init__(self) -> None:
        self.name = "paritosh"
        self.rollno = 101
        self.course = "MCA"

s1 = Student()
print(s1.name,s1.rollno,s1.course)
print(Student.__doc__)
# help(Student)   

""" 
    Output:
    paritosh 101 MCA
    This is nothing but doc string and we can print it using __doc__ and help(class_name)

"""