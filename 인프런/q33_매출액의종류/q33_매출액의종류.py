
import sys
input = lambda : sys.stdin.readline().rstrip()

# 슬라이딩 윈도우

N, K = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0

for rt in range(N):
    if (rt - lt + 1) == K:
        print(len(set(arr[lt:rt+1])), end=' ')
        lt += 1



''''
시간초과 뜨는 풀이 
'''