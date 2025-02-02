'''
현재까지 본 최소 가격으로 최대한 멀리 가면 최소 비용

방법: 매 도시마다 가격을 확인해서 최소 가격을 업데이트
'''
N = int(input()) # 도시의 개수 N
dist = list(map(int, input().split())) # N - 1개
prices = list(map(int, input().split())) # 도시별 리터당 가격 N 개

min_sofar = prices[0]
cost = min_sofar * dist[0]

# 이동하면서 현재까지의 최소가격으로 다음 거리만큼 주유하면 최소비용이 소요된다.
for i in range(1, N - 1): # 마지막 가격 제외
    if min_sofar > prices[i]:
        min_sofar = prices[i]
        cost += min_sofar * dist[i]
    else:
        cost += min_sofar * dist[i]

print(cost)