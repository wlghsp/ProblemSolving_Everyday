
from collections import defaultdict

N = int(input())
first = input()
first_word = defaultdict(int)
for w in first:
    first_word[w] += 1
ans = 0

for _ in range(N - 1):
    other = input()
    other_word = defaultdict(int)
    for w in other:
        other_word[w] += 1
    diff = 0
    for k in set(first_word.keys() | other_word.keys()):
        diff += abs(first_word[k] - other_word[k])
    len_diff = abs(len(first) - len(other))

    if diff == 0 or (diff == 1 and len_diff == 1) or (diff == 2 and len_diff == 0):
        ans += 1
print(ans)