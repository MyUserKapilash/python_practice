#Using List Compreensions

input_list=[1,2,3,4,4,5,6,7,7]
output_list=[]

for var in input_list:
        if var % 2 == 0:
                output_list.append(var)

print("output list using for loop:",output_list)


input_list=[1,2,3,4,4,5,6,7,7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("output list using list comprehensions:",list_using_comp)

#Dict Comprehension

input_list=[1,2,3,4,5,6,7]
output_dict={}
for var in input_list:
    if var % 2 !=0:
        output_dict[var]=var**3
print("output Dictionary using for loop:",output_dict)

input_list=[1,2,3,4,5,6,7]
d={var:var**3 for var in input_list if var % 2 !=0}
print("output Dictionary using dictionary comprehensions:",d)

#set comprehension
input_list=[1,2,3,4,4,5,6,6,6,7,7]
output_set=set()

for var in input_list:
    if var % 2 ==0:
        output_set.add(var)
print("output set using for loop:",output_set)


input_list=[1,2,3,4,4,5,6,6,6,7,7]
set_using_com = {var for var in input_list if var % 2 == 0}
print("output set using ser comprehensions:",set_using_com)


#Generater Comprehenson

input_list=[1,2,3,4,4,5,6,6,6,7,7]
output_gen = (var for var in input_list if var % 2 == 0)
print("output valies using generator comrehensions:",end=' ')

for var in output_gen:
    print(var,end=' ')
