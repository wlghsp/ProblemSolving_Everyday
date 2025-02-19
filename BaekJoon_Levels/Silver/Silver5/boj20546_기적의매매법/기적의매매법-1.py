cash = int(input())
prices = list(map(int, input().split()))

j_cash = cash
j_stock = 0
for p in prices:
    if j_cash <= 0:
        break

    if j_cash >= p:
        j_stock += j_cash // p
        j_cash = j_cash % p

jun = j_cash + j_stock * prices[len(prices) - 1]


# 2. seongmin
s_cash = cash
s_stock = 0
for i in range(len(prices) - 3):
    if prices[i] < prices[i + 1] < prices[i + 2]:
        if i + 3 < len(prices) and s_stock > 0:
            s_cash += prices[i + 3] * s_stock
            s_stock = 0
    elif prices[i] > prices[i + 1] > prices[i + 2]:
        if i + 3 < len(prices) and s_cash >= prices[i + 3]:
            buy_cnt = s_cash // prices[i + 3]
            s_stock += buy_cnt
            s_cash -= buy_cnt * prices[i + 3]

seong = s_cash + s_stock * prices[len(prices) - 1]

if jun > seong:
    print("BNP")
elif seong > jun:
    print("TIMING")
else:
    print("SAMESAME")