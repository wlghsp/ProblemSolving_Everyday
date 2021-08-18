# 0 1 2 2 2 7
# 1 0 0 0 0 1

# 2 1 2 1 2 1
# -1 0 0 1 0 7

import sys

input = sys.stdin.readline


original = [1, 1, 2, 2, 2, 8]

numOfPiece = list(map(int, input().split()))

print(*[x - y for x, y in zip(original, numOfPiece)])


print(*[original[i] - numOfPiece[i] for i in range(len(original))])
