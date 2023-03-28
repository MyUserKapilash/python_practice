#Instance Variable

class Student:
    def __init__(self):
        self.name='Mary'
        self.age=20
        self.marks=80
        print("self address:",id(self))
    def talk(self):
        print("hello i am:",self.name)
        print("my age is :",self.age)
        print("my marks are:",self.marks)
        print("self ad inside talk:",id(self))
Student_one=Student()
Student_one.talk()
print("Student_one address:",id(Student_one))

#

class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print("hello my name is:",self.name)
        print("my rollno is :",self.rollno)
        print("my marks are:",self.marks)

Student_one=Student("Mary",101,90)
Student_one.talk()
Student_two=Student("John",102,95)
Student_two.talk()


#Finding Variable instance

class Employee:
    def __init__(self):
        self.eno=100
        self.ename='Tony'
        self.esal=10000
e=Employee()
print(e.__dict__)
print("name of the Employee:",e.ename)


#Intance variable attached

class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t=Test()
t.m1()
print(t.__dict__)

#Adding intance outside of the Object

class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t=Test()
t.m1()
t.d=40
print(t.__dict__)
    












