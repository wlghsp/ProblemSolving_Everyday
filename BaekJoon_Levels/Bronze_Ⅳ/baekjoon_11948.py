import sys

input = sys.stdin.readline


scores1 = [int(input()) for _ in range(4)]
scores2 = [int(input()) for _ in range(2)]

scores1.sort(reverse=True)
scores2.sort(reverse=True)
result = sum(scores1[0:3]) + scores2[0]
print(result)
