my_list = [] # empty list called my_list

#append the following element to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#insert the value 15 in the second postion
my_list.insert(1,15)
print(my_list)
 # extend the list  with another list
my_list.extend([50,60,70])
print(my_list)
#removed the last element for my_list
my_list.pop() 
print(my_list)
# sort in ascending order
my_list.sort()
print(my_list)
 #find and print the value of the 30 in my-list
index_of_30 = my_list.index(30)
print("index of 30", index_of_30)

