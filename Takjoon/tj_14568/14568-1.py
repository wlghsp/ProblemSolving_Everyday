import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

"""
- c = b + 2
- a != 0 and b != 0 and c != 0
- A % 2 == 0
"""

N = int(input())

cnt = 0
for a in range(2, N, 2):
    for b in range(1, N):
        for c in range(1, N):
            
            if c >= b + 2 and a + b + c == N:
                cnt += 1
print(cnt)