# Complete the breakingRecords function below.
def breakingRecords(scores):
    minScore = scores[0]
    maxScore = scores[0]
    maxBroken = 0
    minBroken = 0
    for i in scores[1:]:
        if i > maxScore:
            maxBroken += 1
            maxScore = i
        elif i < minScore:
            minBroken += 1
            minScore = i
        else:
            continue
    return maxBroken, minBroken


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores))
