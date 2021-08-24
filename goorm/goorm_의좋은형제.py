import sys


input = sys.stdin.readline


n1, n2 = map(int, input().split())
day = int(input())


for i in range(day):
    if i % 2 == 0:
        if n1 % 2 != 0:
            jin_give = n1//2 + 1
            n2 += jin_give
            n1 -= jin_give
        else:
            jin_give = n1//2
            n2 += jin_give
            n1 -= jin_give
    else:
        if n2 % 2 != 0:
            sun_give = n2//2 + 1
            n2 -= sun_give
            n1 += sun_give
        else:
            sun_give = n2//2
            n2 -= sun_give
            n1 += sun_give

print(n1, n2)
