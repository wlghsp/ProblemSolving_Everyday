
"""
Idea:


"""

import sys

input = lambda: sys.stdin.readline().rstrip()
dict = {}
for i in range(8):
    dict[i + 1] = int(input())
sorted_dict = sorted(dict.items(), key=lambda x: -x[1])
total = 0
result = []
for i in sorted_dict[:5]:
    total += i[1]
    result.append(i[0])
print(total)
print(*sorted(result))
