#OverLoding Method
#defining method with same name but different arguments 
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        print("id of b_one inside megic method is:",id(self))
        print("id of b_two inside megic method is:",id(other))
        return self.pages+other.pages
    
b_one=Book(100)
b_two=Book(200)

b_three=b_one+b_two

print("id of b_one is:",id(b_one))
print("id of b_two is:",id(b_two))

#Method OverLoding 

class Test:
    def m_one(self):
        print("this is m_one method")
    def m_one(self,arg):
        print("this is m_one with arg")
t=Test()
t.m_one(18)
