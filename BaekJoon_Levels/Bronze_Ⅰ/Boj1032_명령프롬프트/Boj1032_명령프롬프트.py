import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

file_names = []
for _ in range(N):
    file_names.append(list(input()))

result = file_names[0]
for names in file_names:
    for i in range(len(file_names[0])):
        if names[i] != result[i]:
            result[i] = '?'

print(''.join(result))