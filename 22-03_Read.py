#Read all data on the file
f=open("besant_data.txt",'r')
data=f.read()
print(data)
f.close()

#To read only first 50 Characters
f=open("besant_data.txt",'r')
data=f.read(50)
print(data)
f.close()

#To read line by line
f=open("besant_data.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end=' ')
f.close()
       
