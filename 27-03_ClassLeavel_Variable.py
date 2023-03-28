
class Student:
    school_name="SGVG"

    def __init__(self):
        self.a=100
    def disp(self):
        a=200
        print("the value of a is:",self.a)
        print("the value of a is:",a)


s=Student()
s.disp()
print(s.__dict__)
print(Student.__dict__)
print("school name:",s.school_name)


class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)

t=Test()
t.m1()
t.m2()

#Instance methods

class Student:
    def __init__(self):
        self.a=100
    def disp(self):
        a=200
        print("The value of a is:",self.a)
        print("The value of a is:" ,a)
s=Student()
s.disp()

#Class methods
#class Animal:
#    legs=4
#    @classmethod
#    def walk(cls,name):
#        print('() walks with () legs...:',format(name,cls,legs))
#Animal.walk('dog')
#Animal.walk('cat')


#Startic Method

class CustomMath:
    @staticmethod
    def add(x,y):
        print('the Sum:',x+y)
    @staticmethod
    def product(x,y):
        print('the Product:',x*y)
    @staticmethod
    def avrage(x,y):
        print('the avrage:',(x+y)/2)

CustomMath.add(10,20)
CustomMath.product(10,20)
CustomMath.avrage(10,20)







