from itertools import combinations

N = int(input())
K = int(input())
AB = [tuple(map(int, input().split())) for _ in range(K)]

# Please write your code here.
max_count = 0
for combo in combinations(range(1, 2 * N + 1), N):
    usable = set(combo) # 선택된 용액들을 set으로 관리

    count = 0
    for a, b in AB:
        if a in usable and b in usable:
            count += 1 # 만들 수 있으면 카운트 증가

    max_count = max(max_count, count)

print(max_count)




"""
3
6
1 1
1 2
2 3
4 5
2 4
5 6

3
"""