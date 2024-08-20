#create an empty list
my_list = []
# print(my_list)

#appending elements to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print(my_list)

#insert 15 at the second position
my_list.insert(1, 15)
# print(my_list)

#extend list with another list
my_list.extend([50, 60, 70])
# print(my_list)

#remove last item from list
my_list.pop()
# print(my_list)

#sorting my list in ascending order
my_list.sort()
# print(my_list)

#getting index of values
print(my_list)
print(my_list.index(30))
