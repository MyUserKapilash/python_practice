list_tup=[(100,"a"),(200,"b"),(300,"c"),(400,"d"),(500,"e")]
d2=dict(list_tup)
print(d2)
print(len(d2))

print(d2[400])

value=d2.get(300)
print(value)

value=d2.get(600)
print(value)

value2=d2.get(200,0)
print(value2)

value3=d2.get(700,0)
print(value3)


d2.pop(100)
print(d2)

r=d2.pop(800,0)
print(r)

d2.popitem()
print(d2)

print("key:",d2.keys())
print("value:",d2.values())
print("items:",d2.items())


d3=d2
print(d3)
d4=d2.copy()
print(d4)
