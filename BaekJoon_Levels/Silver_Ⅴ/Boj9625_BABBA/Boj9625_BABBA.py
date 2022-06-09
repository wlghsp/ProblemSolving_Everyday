import sys
input = lambda : sys.stdin.readline().rstrip()

k = int(input())

a = [1, 0]
b = [0, 1]

for i in range(2, k+1):
    a.append(a[i - 1] + a[i - 2])
    b.append(b[i - 1] + b[i - 2])

print(a[k], b[k])