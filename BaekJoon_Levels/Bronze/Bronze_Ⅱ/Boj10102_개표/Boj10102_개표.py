import sys
input = lambda : sys.stdin.readline().rstrip()

V = int(input())
votes = input()

a = votes.count('A')
b = votes.count('B')

if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')
