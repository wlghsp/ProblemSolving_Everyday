"""
3 1

2 1

"""

import sys

input = lambda: sys.stdin.readline().rstrip()

sumOfScores, gapofScores = map(int, input().split())

result = []
for i in range(sumOfScores + 1):
    for j in range(sumOfScores + 1):
        if (i + j) == sumOfScores and i - j == gapofScores:
            scores = f"{i} {j}"
            result.append(scores)

if not result:
    print(-1)
else:
    print(*result)
