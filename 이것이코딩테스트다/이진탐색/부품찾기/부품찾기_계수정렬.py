
import sys
input = lambda: sys.stdin.readline().rstrip()


# 가게에 있는 물품
n = int(input()) # 가게에 있는 부품의 개수
store = [0] * 1000001 # 가게의 물품 list (0으로 초기화)

# 가게에 있는 물품 check(있는 경우 1을 할당)
for i in list(map(int, input().split())):
    store[i] = 1


# 손님이 원하는 물품
m  = int(input()) # 손님이 찾는 부품의 개수
customer = list(map(int, input().split())) # 손님이 원하는 부품 list


# 손님이 찾는 부품과 가게의 부품 비교 (있으면 1, 없으면 0)
for i in customer:
    if store[i] ==1:
        print('Yes', end=' ')
    else:
        print('no', end=' ')





