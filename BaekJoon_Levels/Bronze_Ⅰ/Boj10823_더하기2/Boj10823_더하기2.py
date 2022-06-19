import sys
input = lambda : sys.stdin.readline().rstrip()

list = []
while True:
    s = input()
    if s == '':
        break
    list.append(s)

sen = ''.join(list)
result = sum(map(int, sen.split(',')))

print(result)