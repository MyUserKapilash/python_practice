#Single inheritance
class P:
    def m1(self):
        print("Perant method")
class C(P):
    def m2(self):
        print("Child method")

c=C()
c.m1()
c.m2()

#Multiful Inheritance

class P:
    def m1(self):
        print("Parent method")
class C(P):
    def m2(self):
        print("Child method")
class CC(C):
    def m3(self):
        print("Sub Child method")
    def m1(self):
        print("GrandChild m1")

c=CC()
c.m1()
c.m2()
c.m3()

#multiful Inhetitance
class P1:
    def m1(self):
        print("parent method")
class P2:
    def m2(self):
        print("Parent2 method")
    def m1(self):
        print("Parent2 method")
class C(P2,P1):
    def m3(self):
        print("Child2 method")

c=C()
c.m1()
c.m2()
c.m3()



