



N = int(input())

scores = list(map(int, input().split()))
rank = [1 for _ in range(len(scores))]

for i in range(len(scores)):
    for j in range(len(scores)):
        if scores[i] < scores[j]:
            rank[i] += 1

print(*rank)