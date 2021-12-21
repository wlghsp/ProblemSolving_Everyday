
'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
입력

첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
출력

첫째 줄에 N!을 출력한다.

10  

3628800


'''
import sys

input = lambda: sys.stdin.readline().rstrip()

def f(num):
    if num <=1: #  0이 들어 올 경우에 대비 
        return 1
    return num * f(num-1)


n = int(input())

print(f(n))

