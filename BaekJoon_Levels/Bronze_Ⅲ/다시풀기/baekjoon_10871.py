import sys
input = sys.stdin.readline


n, x = map(int, input().split())

c = list(map(int, input().split()))
# list로 감싸면 바로 리스트에 숫자들을 분리하여 넣어줄 수 있다.

for i in range(n):
    if c[i] < x:
        print(c[i], end=" ")
