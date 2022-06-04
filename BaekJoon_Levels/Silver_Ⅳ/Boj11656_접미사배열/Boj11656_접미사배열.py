

import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()

list = []
for i in range(len(S)):
    list.append(S[i:])

for word in sorted(list):
    print(word)

