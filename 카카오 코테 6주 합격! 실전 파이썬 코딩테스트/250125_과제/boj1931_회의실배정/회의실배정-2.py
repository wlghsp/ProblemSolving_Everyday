import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
prev = 0
for start, end in meetings:
    if start >= prev:
        cnt += 1
        prev = end
print(cnt)

'''
1. 명제: 끝나는 시간이 빠른 회의를 먼저 진행하면 최대 회의 개수
2. 부정: 끝나는 시간이 빠르지 않은 회의를 먼저 진행해도 최대 회의 개수
3. 모순:

[(1, 3), (2, 6), (3, 4), (4, 5)] 
위 순서대로 진행하면  2개 가능

[(1, 3), (3, 4), (4, 5), (2, 6)] 
끝나는 시간이 빠른 부터 3개 가능

부정이 모순이므로 명제는 참이다.
'''