import sys

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
memo_keywords = set(input() for _ in range(N))

res = []
for _ in range(M):
    words = input().split(",")
    for w in words:
        memo_keywords.discard(w) # distcard 가 remove 보다 안전. 없으면 무시함
    res.append(len(memo_keywords))

print(*res, sep='\n')