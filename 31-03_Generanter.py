#Create Generater Function
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i

a=sq_numbers(3)
print("a:",type(a))
print("the square of numbers 1,2,3 are:")
print(next(a))
print(next(a))
print(next(a))

#Using Generate Funtion
def gen():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    yield "E"
    yield "F"
    yield "G"
    yield "H"
#Inside of using Interer funtion using generter
g=gen()
for a in g:
    print(a)
    
      
g = (x*x for x in range(1000000000000))
print(type(g))

for n in g:
    print(n)

