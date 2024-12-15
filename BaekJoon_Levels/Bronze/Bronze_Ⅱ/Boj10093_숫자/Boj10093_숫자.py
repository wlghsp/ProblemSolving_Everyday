import sys
input = lambda : sys.stdin.readline().rstrip()
a, b = map(int, input().split())
'''
a가 b보다 큰 경우가 있을 수 있어
a 와 b 중 어느 쪽이 큰지를 확인
'''
if a > b:
    small = b
    big = a
else:
    small = a
    big = b

arr = [i for i in range(small+1, big)]
print(len(arr))
print(*arr)
