
"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.


3 16

3
5
7
11
13


"""



import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 1000000

# 수를 지웠는지 아닌지 기록하는 리스트
check = [0] * (MAX +1)
check[0] = check[1] = True

for i in range(2,MAX+1):
    if not check[i]:
        j = i+i;
        while j <= MAX:
            check[j] = True
            j += i



m, n = map(int, input().split())

for i in range(m, n+1):
    if not check[i]:
        print(i)
