import sys
input = sys.stdin.readline

N = int(input())
odd = N - N//2
even = N//2

for i in range(N):
    print("* " * odd)
    print(" *" * even)
