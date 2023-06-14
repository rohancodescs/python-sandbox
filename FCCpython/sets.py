#Sets: unordered, mutable, no duplicates
mySet = {1 ,2 ,3 ,1 ,2}
print(mySet) #output: {1, 2, 3}

mySet = set("Hello") #creates set from string, outputs {'e', 'l', 'H', 'o'} or in some random order not duplicating the l ("l" only appears once)
print(mySet)

mySet.add(1)
print(mySet)
mySet.remove(1)
print(mySet)

print("\n-------------------------\n")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
print(odds.intersection(evens)) #output: set()
print(odds.union(evens)) #output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#you can use these methods to update the sets as well

odds.intersection_update(primes)
print(odds) #output: {3, 5, 7}
evens.symmetric_difference_update(primes)
print(evens) #output: {0, 2, 4, 6, 8}

print("\n-------------------------\n")

list1 = {1, 2, 3, 4, 5, 6}
list2 = {4,5,6}
print(list1.issubset(list2)) #output: False
print(list1.issuperset(list2)) #output: True