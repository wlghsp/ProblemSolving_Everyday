import string
import math

def solution(n, k):
    answer = 0
    # 1. k 진수 변환
    temp = string.digits
    def convert(num, base):
        if num == 0:
            return '0'
        res = ''
        while num != 0:
            num, mod = divmod(num, base)
            res = temp[mod] + res
        return res
    S = convert(n, k)

    def is_prime(num):
        num = int(num)
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if  num % i == 0:
                return False
        return True

    # 2. 탐색하여 조건에 맞는 소수 찾아 갯수 리턴
    for num in S.split('0'):
        if not num: continue
        if is_prime(num):
            answer += 1

    return answer


print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2