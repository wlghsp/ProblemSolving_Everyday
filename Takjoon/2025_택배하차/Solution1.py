from collections import deque
import sys, os
sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

packages = []
for _ in range(M):
    k, h, w, c = map(int, input().split())
    packages.append((k, h, w, c))

grid = [[0] * (N + 1) for _ in range(N + 1)]
pkg_info = {}  # k -> (h, w, top_row, left_col)

def drop_package(k, h, w, c):
    # 택배를 격자에 투하하여 안착시킴
    pass

def apply_gravity():
    # 택배 제거 후 떠 있는 택배들을 아래로 떨어뜨림
    pass

def can_remove_left(k):
    # 택배 k를 왼쪽으로 뺄 수 있는지 확인
    pass

def can_remove_right(k):
    # 택배 k를 오른쪽으로 뺄 수 있는지 확인
    pass

def remove_package(k):
    # 격자에서 택배 k를 제거
    pass

for k, h, w, c in packages:
    drop_package(k, h, w, c)

result = []
remaining = set(k for k, h, w, c in packages)

while remaining:
    left_candidates = sorted([k for k in remaining if can_remove_left(k)])
    if left_candidates:
        k = left_candidates[0]
        remove_package(k)
        remaining.remove(k)
        result.append(k)
        apply_gravity()

    right_candidates = sorted([k for k in remaining if can_remove_right(k)])
    if right_candidates:
        k = right_candidates[0]
        remove_package(k)
        remaining.remove(k)
        result.append(k)
        apply_gravity()

for r in result:
    print(r)
