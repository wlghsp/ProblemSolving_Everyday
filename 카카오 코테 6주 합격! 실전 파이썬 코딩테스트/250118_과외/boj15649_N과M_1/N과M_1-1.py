
n, m = map(int, input().split())


answers = []
def recur(picked, length):
    if length == m:
        answers.append(picked)
        return

    for i in range(1, n + 1):
        if i in picked: continue

        recur(picked + [i], length + 1)


recur([], 0)
for answer in answers:
    print(*answer, sep=' ')
