import sys
input = sys.stdin.readline

scores = []
for _ in range(5):
    a = int(input())
    if a > 40:
        scores.append(a)
    else:
        scores.append(40)

print(sum(scores)//len(scores))
