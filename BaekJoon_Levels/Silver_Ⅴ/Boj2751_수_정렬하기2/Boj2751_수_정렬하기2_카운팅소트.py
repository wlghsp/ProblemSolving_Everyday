
# https://st-lab.tistory.com/106


N = int(input())

# 카운팅 소트
'''
-1000000 ~ 1000000
기준점 0 = index 1000000 으로 생각
'''
arr = [False] * 2000001


for i in range(N):
    arr[int(input()) + 1000000] = True

for i in range(len(arr)):
    if arr[i]:
        print(i-1000000)
