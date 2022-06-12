
import sys
input = lambda :sys.stdin.readline().rstrip()
N = int(input())

for _ in range(N):
    a = sorted(list(map(int, input().split()))[1:], reverse=True)
    b = sorted(list(map(int, input().split()))[1:], reverse=True)
    if a > b:
        print("A")
    elif b > a:
        print("B")
    else:
        print("D")


