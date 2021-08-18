import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

m = max(scores)

for i, v in enumerate(scores):
    scores[i] = v/m*100

print(sum(scores)/len(scores))
