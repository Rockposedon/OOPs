# Passing arguments during method calling
class Student:
    def __init__(self,name,course,rollno) :
        self.name = name
        self.course = course
        self.rollno = rollno
s1 = Student('Paritosh','MCA',101)
print(s1.name)
print(s1.course)
print(s1.rollno)

s2 = Student('Ajay','Mtech',201)
print(s2.name,s2.course,s2.rollno)

print(s1)           # --> <__main__.Student object at 0x7f24eac43c10>

"""

	def __init__(self, name,course,rollno):      =>> here  name,course,rollno=> are normal variable  
		self.name = name                         | self.name     = these are instance variable
        self.course = course                     | self.course   =    --------------------
		self.rollno = rollno                     | self.rollno   =    --------------------

		==>>  name,course,rollno => object related instance variable

"""

"""
    Output:
    Paritosh
    MCA
    101
    Ajay Mtech 201
    <__main__.Student object at 0x7fb04d163fd0>
"""