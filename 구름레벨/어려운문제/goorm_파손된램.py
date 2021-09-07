"""
3
256 274 512

1
2

5
128 256 512 1024 2048

0

"""

import sys

input = sys.stdin.readline


n = int(input())
memory_sizes = list(map(int, input().split()))

broken_rams = 0
ram_nums = []
for i, v in enumerate(memory_sizes):
    if (v & (v - 1)) != 0:  # 2의 제곱근 판별, 비트연산으로 제곱근인 수와 그 수의 -1을 한 수를 & 연산함.
        broken_rams += 1  # 2의 제곱수는 &연산을 하게되면 0이나온다.
        ram_nums.append(i + 1)


if broken_rams >= 1:
    print(broken_rams)
    print(*ram_nums)
else:
    print(0)
