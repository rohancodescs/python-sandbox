# #Lists: ordered, mutable, allows duplicate elements
# myList = ["banana", "cherry", "apple"]

# # myList2 = myList.copy()#does deep copy
# myList2 = myList#does shallow copy
# myList[1] = "blackberry"
# print(myList2)

# #check if item is in list:
# if "banana" in myList:
#     print("yes")
# else:   
#     print("no")

# #manipulate list:
# myList.append("lemon") #appends to end
# myList.insert(1, "blueberry") #inserts at index 1, and pushes elements outwards
# myList.pop() #removes last element and returns it
# myList.remove("cherry") #removes first occurence of cherry
# myList.reverse() #reverses list
# myList.sort() #sorts list
# myList.clear() #clears list

#creating lists:
newList = ["DEEZ NUTS"] * 5
newList2 = [0] * 5
combine = newList + newList2
print(combine) #output: ['DEEZ NUTS', 'DEEZ NUTS', 'DEEZ NUTS', 'DEEZ NUTS', 'DEEZ NUTS', 0, 0, 0, 0, 0]
print(combine[::-1]) # means from 1st element to last element in steps of 1 in reverse order, if it was :-1, it would be from last element exclusive to first element in steps of 1 in reverse order

#slicing as mentioned in line 29 uses a colon to separate the start stop, so in slicing the format is [start:stop:step] with step being optional
#slicing can also be used to copy lists, so if you want to copy a list, you can do list2 = list1[:]

#slicing can also be used to reverse a list, so if you want to reverse a list, you can do list2 = list1[::-1], 
# because :: signifies the start and stop, and -1 signifies the step, which is in reverse order

#list comprehension:

before = [1,2,3,4,5,6]
after = [i * i for i in before]
print(after)