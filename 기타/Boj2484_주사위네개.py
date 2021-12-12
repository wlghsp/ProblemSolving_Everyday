









import sys

input = lambda : sys.stdin.readline().rstrip()

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1: return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]: return 10000 + lst[1] * 1000  # 3개가 같은 경우
        return 2000 + (lst[1] + lst[2]) * 500 # 2개 2개 인 경우
    for i in range(3): # 같은눈이 2개인 경우 찾기
        if lst[i] == lst[i+1]: return 1000 + lst[i] * 100
    return lst[-1] * 100



n = int(input())

print(max(money() for i in range(n)))



