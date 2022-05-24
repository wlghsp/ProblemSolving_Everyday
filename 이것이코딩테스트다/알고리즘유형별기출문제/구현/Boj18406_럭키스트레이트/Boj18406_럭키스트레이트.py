
import sys
input = lambda : sys.stdin.readline().rstrip()


N = input()

half = len(N) // 2
first = list(map(int, list(N[:half])))
second = list(map(int, list(N[half:])))

if sum(first) == sum(second):
    print("LUCKY")
else:
    print("READY")