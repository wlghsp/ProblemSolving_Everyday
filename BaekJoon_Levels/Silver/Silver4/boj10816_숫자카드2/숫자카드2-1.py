
def upper_bound(target, cards):
    left, right = 0, len(cards)
    while left < right:
        mid = left + (right - left) // 2

        if cards[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def lower_bound(target, cards):
    left, right = 0, len(cards)
    while left < right:
        mid = left + (right - left) // 2

        if cards[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def count_occurrence(target, cards):
    return upper_bound(target, cards) - lower_bound(target, cards)

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
nums = list(map(int, input().split()))
ans = [count_occurrence(n, cards) for n in nums]

print(*ans, end=' ')