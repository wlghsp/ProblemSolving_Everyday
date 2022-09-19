import sys
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
map = dict()
for _ in range(N):
    url, pw = input().split()
    map[url] = pw


for _ in range(M):
    print(map[input()])
