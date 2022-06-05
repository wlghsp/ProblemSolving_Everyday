


import sys
input = lambda : sys.stdin.readline().rstrip()



n, m = map(int, input().split())

prices = []
for _ in range(m):
    price = tuple(map(int, input().split()))
    prices.append(price)


six_list = sorted(prices, key=lambda x: x[0]) # 6개 패키지 가격이 제일 싼 순서로 정렬한 리스트
one_list = sorted(prices, key=lambda x: x[1]) # 낱개 가격이 제일 싼 순서로 정렬한 리스트

# six_list의 [0][0] 인덱스는 6개 패키지 가격이 가장 싼 물건
# one_list의 [0][1] 인덱스는 낱개 가격이 가장 싼 물건
# 6개 패키지 가격이 더 싸다면
if six_list[0][0] <= one_list[0][1] * 6:
    # 6개 패키지로 일단 구매하고 나머지는 낱개로 산다.
    answer = six_list[0][0] * (n//6) + one_list[0][1] * (n % 6)
    if six_list[0][0] < one_list[0][1] * (n % 6): # 6개 패키지 1개 사는 것이 나머지를 낱개로 사는 것보다 싸다면
        answer = six_list[0][0] * (n//6 + 1)  # 남더라도 모두 6개 패키지로 구매
else: # 6개 패키지가 6개 낱개로 사는 것보다 비싸다면 그냥 전부 다 낱개로 구입
    answer = one_list[0][1] * n

print(answer)