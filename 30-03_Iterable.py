a=[0,5,10,15,20]
for i in a:
    if i % 2 == 0:
        print(str(i)+'is an Even number')
    else:
        print(str(i)+'i an odd number')

l=[1,2,3,4,5]
obj=iter(l)
print("obj datatype:",type(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

#Using Iter & Next method
class Numbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a +=1
        return x

Number_class=Numbers()
Number_iter = iter(Number_class)
