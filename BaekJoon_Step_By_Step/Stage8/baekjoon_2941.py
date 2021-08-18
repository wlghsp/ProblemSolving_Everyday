# 734 893
# 437

import sys
input = sys.stdin.readline
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().strip()

for i in croatia_alphabet:
    if i in word:
        word = word.replace(i, "a")

print(len(word))
