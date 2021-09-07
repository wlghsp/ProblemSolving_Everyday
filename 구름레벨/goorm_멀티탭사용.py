"""
4
7 8 2 3

17

3
10 10 10

20

"""
import sys

input = lambda: sys.stdin.readline().rstrip()


n = int(input())
tabs = input()

blanks = tabs.count(" ")

print(sum(list(map(int, tabs.split()))) - blanks)
