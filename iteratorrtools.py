# from iteratorrtools import product
from itertools import *
a = [1,2]
b = [3,4]
prod = product(a,b)#[(1, 3), (1, 4), (2, 3), (2, 4)]
perm = permutations(a)
comb = combinations(a,2)
comb_w_rep = combinations_with_replacement(a,2)

a = [1,2,3,4]
acc = accumulate(a)
print(list(acc))# [1, 3, 6, 10]

a = [1,2,3,4]
for i in cycle(a):
    #add stop condition
    break
for i in repeat(1,4):
    #add stop condition
    break


