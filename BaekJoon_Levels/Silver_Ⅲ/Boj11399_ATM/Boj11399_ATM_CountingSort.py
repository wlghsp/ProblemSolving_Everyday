import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

# Counting Sort
arr = [0] * 1001
for i in map(int, input().split()):
    arr[i] += 1

prev = 0
sum = 0

for i in range(1001):
    while arr[i] > 0:
        sum += (prev + i)
        prev += i
        arr[i] -= 1

print(sum)