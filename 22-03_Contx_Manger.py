#Using With Function close open file 
with open("besant_data.txt",'a') as f:
    f.write("Benglore\n")
    f.write("City\n")
    f.write("Technology\n")
    print("Is file closed:",f.closed)
print("is file closed:",f.closed)
