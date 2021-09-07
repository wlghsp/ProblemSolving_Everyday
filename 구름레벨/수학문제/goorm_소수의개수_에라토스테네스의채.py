"""
30

10

300

62

"""


import sys
import math

input = lambda: sys.stdin.readline().rstrip()

# 에라토스테네스의 채는 소수 갯수를 구하기에는 좋으나, 소수 판별하는 방법은 아님
def primenums(n):
    array = [True for _ in range(n + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

    # 소수 리스트를 구하는 코드
    # result = []
    # for i in range(2, n + 1):
    #     if array[i]:
    #         result.append(i)

    # 소수 갯수를 구하는 코드
    result = 0
    for i in range(2, n + 1):
        if array[i]:
            result += 1
    return result


n = int(input())

print(primenums(n))
