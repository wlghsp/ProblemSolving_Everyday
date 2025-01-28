N, M = map(int, input().split()) # N: 나무의 수, M: 가져가려는 나무의 길이
tree_heights = list(map(int, input().split()))

def can_take_enough_tree(setting_height):
    total = sum(h - setting_height for h in tree_heights if h > setting_height)
    return total >= M

answer = 0
# 가장 높은 나무를 최댓값으로 설정하여 해당 범위만 탐색
# 절단기의 높이가 가장 높은 나무를 넘어서면 아무것도 가져갈 수 없다.
l, r = 0, max(tree_heights)
while l <= r:
    mid = l + (r-l) // 2
    if can_take_enough_tree(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)

