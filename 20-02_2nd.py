

#Num list
num_list=[]
print("num_list:",num_list)
print("datatype:",type(num_list))
num_list2=list()
print("num_list2:",num_list2)
num_list3=list[1,2,3,4,5,5]
print("num_list3:",num_list3)


#Range
num_list4=list(range(1,11))
print("num_list4:",num_list4)
even_num=list(range(0,21,2))
print("even_num:",even_num)
odd_num=list(range(1,21,2))
print("odd_num:",odd_num)


#Headrogeunious
data_list=[1,2,3,4,"pune",True,3.14,5+7j,[11,22]]
print("data_type:",data_list)
print("Lenght of list:",len(data_list))
print(data_list[4])
print(data_list[1:4])


#Iterate
for data in data_list:
    print(data)
