a=30
b=20
print(a>b)
a=30
b=40
print(a>b)


roll_number=101
print(roll_number==101)
print(roll_number!=500)


a=50
b=40
c=60
print(a>b and b>c)
print(a>b and c>b)
print("or:",a>b or c>b)
print(" q:",a>b or b>c)
print("not:",not(a>b or b>c))

a=90
print("a:",a)
a=a+10
print("a:",a)
a+=10
print("a:",a)

a*=2
print("a:",a)


l1=[1,2,3,4]
l2=[1,2,3,4]
print(l1 is not l2)
print(l2 is l1)


print(l1==l2)

l3=[1,2,3,4,5]
print(4 in l3)
print(10 in l3)
print(4 not in l3)
