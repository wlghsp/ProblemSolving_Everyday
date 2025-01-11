import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input()) # 수열의 크기
nums = list(map(int, input().split())) # 홍준이가 칠판에 적은 수
M = int(input()) # 질문의 갯수
# M 개의 줄에 홍준이가 명우에게 할 질문 S와 E가 주어짐
