
import sys
input = lambda: sys.stdin.readline().rstrip()


n = int(input())

store = set(map(int, input().split()))

m = int(input())
customer = list(map(int, input().split()))



for i in customer:
    if i in store:
        print('Yes', end=' ')
    else:
        print('no', end=' ')