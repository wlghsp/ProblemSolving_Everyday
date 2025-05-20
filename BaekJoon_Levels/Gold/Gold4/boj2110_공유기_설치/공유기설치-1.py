N = int(input())
X = [int(input()) for _ in range(N)]

X.sort()

l, r = 1, X[-1]

while l < r:
    # 공유기 간의 최소 거리
    mid = l + (r - l) // 2
