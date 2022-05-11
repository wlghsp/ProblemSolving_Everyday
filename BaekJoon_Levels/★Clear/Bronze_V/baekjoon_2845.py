
""" 
1 10
10 10 10 10 10

0 0 0 0 0

5 20
99 101 1000 0 97

-1 1 900 -100 -3


출력
상근이가 계산한 참가자의 수와
각 기사에 적혀있는 참가자의 수의 차이

"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
paperNums = list(map(int, input().split()))

numOfParticipants = n * m

print(*list(map(lambda s: s - numOfParticipants, paperNums)))
