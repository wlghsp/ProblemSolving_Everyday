import sys

input = lambda: sys.stdin.readline().rstrip()

L = int(input())  # 롤케이크의 길이
N = int(input())  # 방청객의 수
roll_cake = [0] * L

people = []
maxVal = 0
expected_person = 0
for i in range(N):
    p, k = map(int, input().split())
    cake = k - p
    if cake > maxVal:
        maxVal = cake
        expected_person = i + 1
    people.append((p, k))

ans = 0
in_reality = 0
for i, v in enumerate(people):
    cnt = 0
    for j in range(v[0] - 1, v[1]):
        if roll_cake[j] == 0:
            roll_cake[j] = i + 1
            cnt += 1
    if cnt > ans:
        ans = cnt
        in_reality = i + 1
print(expected_person)
print(in_reality)
