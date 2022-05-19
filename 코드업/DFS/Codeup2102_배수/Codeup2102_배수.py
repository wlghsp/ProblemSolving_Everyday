"""
자연수 N이 입력될 때, 0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력하시오.

입력
자연수 N이 입력된다(N<264)

출력
0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력한다. 이때 출력되는 자연수의 맨 앞자리는 1이어야 한다. 
조건을 만족하는 자연수가 unsigned long long형의 범위에 없을 경우 0
을 출력한다.

입력 예시   
3

출력 예시
111


"""

import sys, math

input = lambda: sys.stdin.readline().rstrip()

minVal = math.inf # 양의 무한대 (최소값 찾기이므로 초기값을 최대값으로 집어넣음)
limit = 11111111111111111111
N = int(input())

def solution(start):
    global minVal, limit, N
    if start % N == 0:
        minVal = minVal if minVal < start else start
    if start > limit // 10:
        return
    solution(start * 10+1)
    solution(start * 10)

solution(1)

print(0) if minVal == math.inf else print(minVal)
