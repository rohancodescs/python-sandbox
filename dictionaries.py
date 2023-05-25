# #dictionaries: unordered, mutable, no duplicate keys, key-value pairs
# hashmap = {"rohan" : 20, "jaden" : 19, "aaryan" : 19, "bhavin" : 50}
# myDict = dict(rohan=20, jaden=19, aaryan=19, bhavin=50)#create dictionary from variables

# emailIndex = "6" 
# email = "rohan@balls.com"

# hashmap[emailIndex] = 5 #adds new key-value pair
# hashmap[emailIndex] = email #THIS WORKS TOO IDK WHY ITS ERRORING
# print(hashmap)

# #deleting items
# del hashmap["rohan"]
# del hashmap[emailIndex]
# print(hashmap)

# hashmap.pop("jaden") #another way to delete items
# hashmap.popitem() #removes last item inserted into hashmap

hashmap = {"rohan" : 20, "jaden" : 19, "aaryan" : 19, "bhavin" : 50}
if "rohan" in hashmap.keys(): #checks if key is in hashmap
    print("yes!")
if 20 in hashmap.values(): #checks if value is in hashmap
    print("yes")
for key, value in hashmap.items(): #iterates through hashmap
    print(key, value)

hashmap["grades"] = ["A", "A", "B+", "B+", "D+", "C+"]
print(hashmap["grades"])
print(hashmap["grades"][0])

#you can use an entire tuple as a KEY, but you cannot use a LIST as a key because lists are mutable and tuples are immutable
