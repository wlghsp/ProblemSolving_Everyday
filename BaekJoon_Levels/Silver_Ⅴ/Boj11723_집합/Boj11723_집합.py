

import sys

input = lambda : sys.stdin.readline().rstrip()

M = int(input())

S = set()

for _ in range(M):
    command = input().split()
    if command[0] == "add":
        S.add(command[1])
    elif command[0] == "remove" and command[1] in S:
        S.remove(command[1])
    elif command[0] == "check":
        if command[1] in S:
            print("1")
        else:
            print("0")
    elif command[0] == "toggle":
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    elif command[0] == "all":
        # S.clear()
        S = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        S.clear()
