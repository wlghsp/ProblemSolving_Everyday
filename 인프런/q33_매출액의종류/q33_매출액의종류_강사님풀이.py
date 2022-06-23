
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

# 슬라이딩 윈도우

N, K = map(int, input().split())
arr = list(map(int, input().split()))

'''
딕셔너리에 숫자의 빈도를 기록하고 
사이즈를 재서 출력한다. 
그리고 0일때는 삭제를 해준다. 
'''
hm = defaultdict(int)
for i in range(K - 1):
    hm[arr[i]] += 1

lt = 0

answer = []
for rt in range(K-1, N):
    hm[arr[rt]] += 1
    answer.append(len(hm))
    hm[arr[lt]] -= 1
    if hm.get(arr[lt]) == 0: # 0이 되었다면 삭제해줘야 길이를 정확히 잴 수 있음
        del hm[arr[lt]]
    lt += 1

print(*answer)