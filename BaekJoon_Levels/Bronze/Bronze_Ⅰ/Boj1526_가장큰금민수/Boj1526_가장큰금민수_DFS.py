import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
result = 0


def DFS(number):
    global result
    if number > N: return
    result = max(result, number)
    DFS(number * 10 + 4)
    DFS(number * 10 + 7)

DFS(4)
DFS(7)
print(result)




