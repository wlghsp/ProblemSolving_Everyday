import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a = list(input())
    a[0] = a[0].upper()
    print(''.join(a))
