import math

B, C, D = map(int, input().split())
burger_price = list(map(int, input().split()))
side_price = list(map(int, input().split()))
drink_price = list(map(int, input().split()))
burger_price.sort(reverse=True)
side_price.sort(reverse=True)
drink_price.sort(reverse=True)
original_price = sum(burger_price) + sum(side_price) + sum(drink_price)
min_set_cnt = min(B, C, D)

discount_price = 0
set_original_price = 0
for i in range(min_set_cnt):
    set_original_price += (burger_price[i] + side_price[i] + drink_price[i])

left_price = original_price - set_original_price

print(original_price)
print(math.trunc(set_original_price * 0.9 + left_price))