#Creating an empty number list
my_list = []
print(my_list)

#Append the following elements to my_list: 10, 20, 30, 40
#empty list my_list = [] 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Insert the value 15 at the second position in the list.
my_list.insert(1,15) #index 1 is the second place
print(my_list)

#Extend my_list with another list: [50, 60, 70].
my_list = [10, 20, 30, 40]
print("List1:", my_list)

another_list = [50, 60, 70]
print("List2:", another_list)

#extending the list by joining them
my_list.extend(another_list)

print("List after append:", my_list)

#Remove the last element from my_list. 
del my_list[-1]
print(my_list)

#Sort my_list in ascending order.
my_list = [10, 20, 30, 40, 50, 60]
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
my_list = [10, 20, 30, 40, 50, 60]
index_of_30 = my_list.index(30)
print(index_of_30)