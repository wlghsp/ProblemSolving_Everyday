import sys
input = sys.stdin.readline


a = input()
b = input()
a = int(a)
fullnum = int(b)
lastnum = int(b[2])
secondnum = int(b[1])
firstnum = int(b[0])
print(a * lastnum)
print(a * secondnum)
print(a * firstnum)
print(a * fullnum)
