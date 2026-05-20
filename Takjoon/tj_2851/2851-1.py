import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

mushrooms = []
for _ in range(10):
    m = int(input())
    mushrooms.append(m)
    
candidates = []
total = 0
for i in range(10):
    total += mushrooms[i]
    candidates.append(total)
    if total >= 100:
        break
    
ans = candidates[-1]
min_diff = float('inf')
for c in candidates[::-1]:
    diff = abs(c - 100)
    if diff < min_diff:
        min_diff = diff
        ans = c
print(ans)
    