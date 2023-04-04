print("Hello")
print(10/0)
print("Hi")

#TRY: 
print("stmt-1")

try:
    
    print(9/3)
    print("code execution")

except ZeroDivisionError:
    
    print(10/2)
    
print("stmt-3")


#Finally
try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number:"))
    print(x/y)
except ZeroDivisionError:
    print("can't divide Zero")
except ValueError:
    print("Please provide int value only")

#try: using only on time
#except: using multiful time
#Finally using only one time
#Exception Occord 
try:
    print("try")
    print(10/0)
except:
    print("except")
finally:
    print("finally")

try:
    print("try")


#Exception not Occord  
try:
    print("try")
except:
    print("except")
finally:
    print("finally")

try:
    print("try")
































































































































































































































































































