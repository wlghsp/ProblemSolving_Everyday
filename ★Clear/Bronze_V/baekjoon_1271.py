import sys

input = sys.stdin.readline
""" 
입력
1000 100

출력
10
0

n 최백준 조교가 가진 돈
m 돈을 받으러 온 생명체의 수

출력
첫 번째 줄 한 생명체에게 돌아가는 돈의 양
두 번째 줄 1원씩 분배할 수 없는 남은 돈 

"""
n, m = map(int, input().split())

firstLine = n // m
second_line = n % m
print(firstLine)
print(second_line)
