import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
cows = [-1] * (N + 1) # -1은 아직 위치를 입력하지 않은 상태
cnt = 0
for _ in range(N):
    cow_num, loc = map(int, input().split())
    if cows[cow_num] == -1:
        cows[cow_num] = loc
    elif cows[cow_num] != loc: # 위치가 다르므로 소가 위치를 바꾼 경우
        cnt += 1
        cows[cow_num] = loc
print(cnt)