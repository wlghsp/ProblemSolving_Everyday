cash = int(input())
prices = list(map(int, input().split()))

j_cash = cash
j_stock = 0
for p in prices:
    if j_cash >= p:
        j_stock += j_cash // p
        j_cash = j_cash % p

s_cash = cash
s_stock = 0
for i in range(3, len(prices)):
    if prices[i - 3] < prices[i - 2] < prices[i] and s_stock > 0:
        s_cash += prices[i + 3] * s_stock
        s_stock = 0
    elif prices[i - 3] > prices[i - 2] > prices[i - 1] and s_cash >= prices[i]:
        buy_cnt = s_cash // prices[i]
        s_stock += buy_cnt
        s_cash -= buy_cnt * prices[i]
last_price = prices[len(prices) - 1]
jun = j_cash + j_stock * last_price
seong = s_cash + s_stock * last_price

if jun > seong:
    print("BNP")
elif seong > jun:
    print("TIMING")
else:
    print("SAMESAME")