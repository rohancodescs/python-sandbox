#lambda arguments: expression
from functools import reduce
# add10 = lambda x: x+10
# print(add10(5))

# #equivalent to:
# def add10_func(x):
#     return x+10

# mult = lambda x,y: x*y
# print(mult(2,7))

# points2D = [(1,2), (15,1), (5,-1), (10,4)]

# def sort_by_y(x):
#     return x[1]
# points2D_sorted = sorted(points2D, key=sort_by_y)
# print("points2D_sorted: ", points2D_sorted)
# print("points2D: ", points2D)

#Map function: map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print("b: ", list(b))

c = [x*2 for x in a]
print("c: ", c) #same as b

#Filter function: filter(func, seq)
b = filter(lambda x: x%2==0, a)
print("b: ", list(b))

c = [x for x in a if x%2==0]
print("c: ", c)

#Reduce function: reduce(func, seq)
a = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, a)
print("product_a: ", product_a)