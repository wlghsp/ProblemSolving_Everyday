import sys


input = sys.stdin.readline


sen = input().rstrip()

a, b = map(int, input().split())

print(sen[a-1:a+b-1])
