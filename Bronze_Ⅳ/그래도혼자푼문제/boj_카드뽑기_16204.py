"""
4 3 2

3

10 0 10

0

5 3 3

5

7 5 2

4

n 개 카드 

m개 카드 앞면 O 가 한 개 

n-m개 카드 앞면 x 한 개

O는 k개, x는 n-k개

7 개 카드 
5 개 카드 앞면 o 한 개 
2 개 카드 앞면 x 한 개

o  3개
x  2개

"""

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())

# 1. 내 풀이
front = ["o" for _ in range(m)] + ["x" for _ in range(n - m)]
back = ["o" for _ in range(k)] + ["x" for _ in range(n - k)]
count = 0
for i in range(n):
    if front[i] == back[i]:
        count += 1
print(count)

# 2. 블로그 참조 간단한 풀이
print(min(m, k) + min(n - m, n - k))
