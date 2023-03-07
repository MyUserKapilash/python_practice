#d={"name":"Ram","Age":22}
#print(d)

d1={}
print("datatype:",type(d1))
print(d1)

d1["city"]="Delhi"
print(d1)

d1["country"]="India"
print(d1)
print(d1["country"])
print(d1["city"])
#print(d1["Salary"])



for key,value in d1.items():
    print(key,value)

for i in d1.items():
    print(i)

d1.clear()
print(d1)

