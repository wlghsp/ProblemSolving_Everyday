T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    max_price = prices[-1]
    for price in reversed(prices):
        max_price = max(max_price, price)
        if price < max_price:
            profit += max_price - price
    print(profit)
