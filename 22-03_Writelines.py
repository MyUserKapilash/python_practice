#Writelines 
f=open("besant_data.txt",'a')
list=["python\n","HTML\n","Javascript\n","data scince"]
f.writelines(list)
print("list of lines written to the file successfully")
f.close()
      
