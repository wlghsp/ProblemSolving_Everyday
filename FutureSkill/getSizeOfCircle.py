# 5   78.53981633974483
# 원의 넓이 = 반지름의 길이 x 반지름의 길이 x π(3.141592...)

import math
def getSize(n):
    return n * n * math.pi


n = int(input()) # n은 반지름의 길이 
print(getSize(n))
