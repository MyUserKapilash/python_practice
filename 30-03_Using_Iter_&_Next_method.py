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
print("Number iter:",type(Number_iter))

print(next(Number_iter))
print(next(Number_iter))
print(next(Number_iter))
print(next(Number_iter))
print(next(Number_iter))

#Using StopIteraation

class Numbers:
    def __iter__(self):
         self.a=1
         return self

    def __next__(self):
      if self.a<=20:
        x=self.a
        self.a +=1
        return x
      else:
        raise StopIteration


