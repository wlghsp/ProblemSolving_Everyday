import sys
from itertools import combinations

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
prohibited = set()
# 1. 금지된 조합을 set으로 저장(O(1) 조회 가능)
for _ in range(M):
    a, b = map(int, input().split())
    prohibited.add((a, b))
    prohibited.add((b, a)) # (b, a)도 동일한 금지 조합!

ans = 0
# 2. 모든 3가지 조합을 생성 (조합은 O(N^2)으로 가능)
for a, b, c in combinations(range(1, N + 1), 3):
    if (a, b) in prohibited or (b, c) in prohibited or (a, c) in prohibited:
            continue # 금지된 조합이면 건너뛰기
    ans += 1

print(ans)
