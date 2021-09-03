"""
a 시작 값
m 곱할 값
d 더할 값
n 몇번째 수 


"""

a, m, d, n = map(int, input().split())


i = a

for _ in range(1, n):
    i = i * m + d

print(i)
