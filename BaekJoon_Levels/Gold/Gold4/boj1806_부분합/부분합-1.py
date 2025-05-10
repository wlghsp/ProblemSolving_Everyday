
N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
total = 0
INF = float('inf')
min_length = INF

for right in range(N):
    total += arr[right]

    while total >= S: # 조건을 만족함
        min_length = min(min_length, right - left + 1)
        # 더 짧은 구간을 찾기 위해 left를 앞으로 당김
        total -= arr[left]
        left += 1

print(0 if min_length == INF else min_length)