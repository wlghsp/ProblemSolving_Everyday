# 6자리의 고유번호
# 첫 5자리는 00000~99999
# 6째 자리는 검증수, 5개의 숫자를 각각 제곱한 수의 합 % 10

# 0 4 2 5 6
# 1

import sys

input = sys.stdin.readline

fiveNums = sum(list(map(lambda s: s ** 2, list(map(int, input().split()))))) % 10
print(fiveNums)
