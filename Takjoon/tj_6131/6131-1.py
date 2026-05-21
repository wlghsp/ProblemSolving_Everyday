import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')


N = int(input())


"""
1. A >= B
2. A^2 = B^2 + N 
"""
ans = 0

for a in range(1, 501):
    for b in range(1, 501):
        if a < b: continue
        res = b * b + N
        if (a * a) == res:
            ans += 1

print(ans)
