import sys

input = sys.stdin.readline


n = int(input())
memory_sizes = list(map(int, input().split()))

broken_rams = 0
ram_nums = []
for memory in memory_sizes:
    if memory % 2 != 0:
        broken_rams += 1
        ram_nums.append(memory)


if broken_rams > 1:
    print(broken_rams)
    print(ram_nums)
