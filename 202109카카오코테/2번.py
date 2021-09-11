"""
양의 정수 n 

k진수 변환 

소수가 몇 개? 



"""


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


import math


def isPrimenum(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


n = 437674
k = 3
# result 3
# n = 110011
# k = 10
# result 2
num = str(convert(n, k))

primenums = []

nums = num.split("0")
nums = [v for v in nums if v]
print(nums)
for n in nums:
    if isPrimenum(int(n)):
        primenums.append(n)
print(primenums)
print(len(primenums))


import math
def isPrimenum(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    
def solution(n, k):
    answer = -1
    num = str(convert(n, k))
    nums = num.split("0")
    nums = [v for v in nums if v]
    primenums = []
    for n in nums:
        if isPrimenum(int(n)):
            primenums.append(n)
    answer = len(primenums)
    return answer
