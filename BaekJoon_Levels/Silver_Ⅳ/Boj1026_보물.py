
import sys

input = lambda : sys.stdin.readline().rstrip()



N = int(input())

a = [ i for i in map(int, input().split())]
b = [ i for i in map(int, input().split())]

a.sort()
# b는 재배치하지 않는다는 조건이 걸려 있다.
# 파이썬 리스트의 pop(인덱스)는 그 해당 인덱스의 요소를 돌려주고 삭제된다. 인덱스 입력 안하면 맨 끝의 요소가 튀어나옴.
sum = 0
for i in range(N):
    x = a[i]
    y = b.pop(b.index(max(b))) # b의 최댓값의 인덱스를 구하고 pop해서 빼주는식으로 내림차순정렬과 같이 값이 추출된다.

    sum += x * y

print(sum)