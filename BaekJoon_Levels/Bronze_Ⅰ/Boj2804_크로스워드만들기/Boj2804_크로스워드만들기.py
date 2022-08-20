
import sys
input = lambda : sys.stdin.readline().rstrip()

a, b = input().split()
r = 0 # a의 공통되는 문자의 위치
c = 0 # b의 공통되는 문자의 위치
for i in range(len(a)):
    index = b.find(a[i])
    if 0 <= index:
        r = index
        c = i
        break
# r 은 b에서의 문자의 인덱스, c는 a에서 일치하는 문자의 위치

for i in range(len(b)):
    for j in range(len(a)):
        if i == r:
            print(a, end='')
            break
        elif j == c:
            print(b[i], end='')
        else:
            print('.', end='')
    print()