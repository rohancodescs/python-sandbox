def add1(lst1):
    ret = []
    for x in lst1:
        ret.append(x + 1)
    return ret

def x2(lst1):
    ret = []
    for x in lst1:
        ret.append(x * 2)
    return ret

def common(lst, f):
    ret = []
    for x in lst:
        ret.append(f(x))
    return ret

def add1(x):
    return x + 1
def add2(x):
    return x + 2
def add(x,y):
    return x + y

