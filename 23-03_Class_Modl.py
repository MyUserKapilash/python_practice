class student:
    def __init__(self,name,roll_no):
          self.name=name
          self.roll_no=roll_no
    def disp_info(self):
        print("student name:",self.name)
        print("roll_no:",self.roll_no)

s1=student("Ram",101)
s1.disp_info()
s2=student("John",102)
s2.disp_info()
