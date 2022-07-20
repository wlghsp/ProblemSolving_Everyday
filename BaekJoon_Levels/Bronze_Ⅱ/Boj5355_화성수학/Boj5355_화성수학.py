import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    line = list(input().split())
    num = float(line[0])
    for o in line[1:]:
        if o == '@':
            num *= 3
        elif o == '%':
            num += 5
        elif o == '#':
            num -= 7
    print(f'{num:.2f}')
