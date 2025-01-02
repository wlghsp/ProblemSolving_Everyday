def check_cards(card_set, queries):
    return ['1' if q in card_set else '0' for q in queries]

N = int(input())
number_cards = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

distinct_nums = set(number_cards)

result = check_cards(distinct_nums, arr)
print(*result)