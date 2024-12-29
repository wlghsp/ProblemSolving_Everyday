from bisect import *

def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x: # 확인해야함
        return i
    else:
        return -1


lst = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70] # sorted list
target = 51
print(index(lst, target))
