
N, K = map(int, input().split())
temps = list(map(int, input().split()))

# 투포인터 슬라이딩 윈도우 풀이

total = sum(temps[:K])
max_total = total
for i in range(K, N):
    total += temps[i] - temps[i - K]
    max_total = max(max_total, total)

print(max_total)