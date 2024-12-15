import sys

input = lambda : sys.stdin.readline().rstrip()


maxVal = float("-inf")
num = 0

for i in range(5):
    total = sum(map(int,input().split()))
    if maxVal < total:
        maxVal = total
        num = i+1


print(num, maxVal)