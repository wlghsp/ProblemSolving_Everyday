import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

heights = []
total = 0
for _ in range(9):
    h = int(input())
    total += h
    heights.append(h)
def getRes():
    res = []
    for a in range(9):
        for b in range(9):
            if a == b: continue
            if (total - heights[a] - heights[b]) == 100:
                for i in range(9):
                    if i == a or i == b: continue
                    res.append(heights[i])     
                return res
    return res
res = getRes()
res.sort()
print(*res, sep='\n')