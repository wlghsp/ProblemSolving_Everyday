
def has_num(num, cards):
    left, right = 0, len(cards) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if cards[mid] == num:
            return True
        elif cards[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
nums = list(map(int, input().split()))
for n in nums:
    print(1 if has_num(n, cards) else 0, end=' ')
