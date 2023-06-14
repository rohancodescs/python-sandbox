import sys
import timeit
#ordered, IMMUTABLE, allows duplicate elements
myTuple = ("rohan", "bhatt", 20)
print(myTuple.count("rohan"))


#can convert tuples to lists and vice versa through casting tuples(list) and lists(tuple)

#unpacking tuples:
firstname, lastame, age = myTuple
print(firstname, lastame, age)

#you may want to use a tuple instead of a list when dealing with large amounts
#of data that you don't want to change, because tuples take up less memory than lists

myTuple = ("rohan", "bhatt", 1, 2, 3, 4, 5, 2103)
myList = list(myTuple)
print(sys.getsizeof(myTuple), "bytes") #104 bytes
print(sys.getsizeof(myList), "bytes") #120 bytes
print("\n-------------------------\n")

#timeit module:
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) #took .005 seconds
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) #took .043 seconds list much longer

