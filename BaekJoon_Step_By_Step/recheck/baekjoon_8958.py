import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
