# #Strings are ordered and immutable; used for text representation

# myStr = "            Hello World!           "
# myStr = myStr.strip() #must reassign myStr to itself to impact it
# print(myStr) #get rid of white space

# myStr = myStr.lower()
# myStr = myStr.upper()
# startsWith = myStr.startswith("H")
# endsWith = myStr.endswith("!")
# print(myStr, startsWith, endsWith)

#get index with .find, will return -1 if it cant find the character
myStr = "Hello World!"
print(myStr.find("World"))#return index where "World" starts
print(myStr.count('l')) 

strToList = "1,2,3,4,5"
list1 = strToList.split(",") #split string into list
print(list1)
listToStr = ",".join(list1) #join list into string
print(listToStr)