"""
s가 60이 되면 0으로 초기화되고, m이 1늘어난다.
m이 60이 되면 0으로 초기화되고, h이 1늘어난다.
h이 24가 되면 0으로 초기화된다. 

"""
import sys

input = sys.stdin.readline

h, m, s = map(int, input().split())
sec = int(input())

# h: 시각, m:분, s:초, sec:추가된 초
# 고려요소 1번째
s1 = (s + sec) % 60
m1 = (s + sec) // 60
# 고려요소 2번째
m2 = (m + m1) % 60 # 최종 분 
h1 = (m + m1) // 60 
# 고려요소 3번째
h2 = (h + h1) % 24 # 최종 시각 

print(h2, m2, s1)









