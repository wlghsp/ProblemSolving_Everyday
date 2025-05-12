from collections import defaultdict

kinds = defaultdict(int)
def add_kind(c):
    kinds[c] += 1
def remove_kind(c):
    kinds[c] -= 1
    if kinds[c] <= 0:
        del kinds[c]

N = int(input())
text = list(input())

left = 0
max_len = 0
for right in range(len(text)):
    add_kind(text[right])

    while len(kinds) > N:
        remove_kind(text[left])
        left += 1

    if len(kinds) <= N:
        max_len = max(max_len, right - left + 1)

print(max_len)
