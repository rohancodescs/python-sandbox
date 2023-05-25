from collections import Counter
from collections import namedtuple, OrderedDict, defaultdict, deque

a = "aaaaabbbbbccccc"
myCounter = Counter(a)
print(myCounter)
print(myCounter.items())


print(myCounter.most_common(1)[0][0])


#named tuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

#Ordered dict is just a dict but remembers order, but is kinda useless cause after 3.7 dicts have ability to be ordered







#deque is a list optimized for inserting and removing items
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop() 
d.popleft()
d.extend([4,5,6])
d.extendleft([7,8,9])

d.rotate(2)#rotate the list to the right by 2
d.rotate(-2)#rotate the list to the left by 2

