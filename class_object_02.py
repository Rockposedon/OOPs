class Student:
    
    '''This is student class with some data'''
    def __init__(self,x,y,z) :
        self.name = x
        self.marks = y
        self.course = z
    
    def Information(self):
        print("student name is {}, his marks is {} and course is {}".format(self.name,self.marks,self.course))

s1 = Student("Rockposedon",90,"BCA")
s1.Information()
print("Print doc string via class: ",Student.__doc__)
print("Print doc string via object: ",s1.__doc__)

"""
    Output:
    student name is Rockposedon, his marks is 90 and course is BCA
    Print doc string via class:  This is student class with some data
    Print doc string via object:  This is student class with some data

"""