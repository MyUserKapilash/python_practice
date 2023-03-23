"""Example: Attributes of file object"""
f=open("ecom_project.txt",'w')
print("file name:",f.name)
print("file mode:",f.mode)
print("is file readabe:",f.readable())
print("is file writable:",f.writable())
print("is file closed:",f.closed)
f.close()
print("is file closed:",f.closed)
