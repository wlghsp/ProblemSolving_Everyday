import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a, b = input().split()
    print('Distances: ', end='')
    for i in range(len(a)):
        x = ord(a[i]) - 64
        y = ord(b[i]) - 64
        if x > y:
            print((y+26) - x, end=' ')
        else:
            print(y-x, end=' ')
    print()