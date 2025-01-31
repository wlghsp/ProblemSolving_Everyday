N = int(input())
times = list(map(int, input().split()))
times.sort()

res = 0
for i in range(N):
    each_one = times[i]
    for j in range(i):
        each_one += times[j]
    res += each_one

print(res)

'''
1. 명제: 인출 시간이 가장 작은 사람부터 줄을 서면 최소 시간
2. 부정: 인출 시간이 작지 않은 사람부터 즐을 서도 최소 시간
3. 모순:

인출에 걸리는 시간 = [2, 4, 1]
2 + (2 + 4) + (2 + 4 + 1) = 15

[1, 2, 4]
1 + (1 + 2) + (1 + 2 + 4) = 11

부정이 모순이므로 명제는 참이다.

'''
