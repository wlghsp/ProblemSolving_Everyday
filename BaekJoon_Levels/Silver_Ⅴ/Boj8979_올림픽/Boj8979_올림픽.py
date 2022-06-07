import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(N)]

sorted_countries = sorted(countries, key=lambda x: (-x[1], -x[2], -x[3]))

idx = 0
for i in range(len(sorted_countries)):
    if sorted_countries[i][0] == K:
        idx = i  # 구하려는 국가의 index를 찾아 놓는다.

# 위에서 찾은 인덱스의 메달성적과 동일한 경우가 나오면 바로 그 인덱스 + 1(등수이므로 1부터 시작)하여 출력한다.
# 성적이 동일한 경우의 등수를 찾고자 함. 파이썬은 슬라이싱으로 리스트를 비교할 수 있어 이런 풀이가 가능함
for i in range(N):
    if sorted_countries[idx][1:] == sorted_countries[i][1:]:
        print(i + 1)
        break
