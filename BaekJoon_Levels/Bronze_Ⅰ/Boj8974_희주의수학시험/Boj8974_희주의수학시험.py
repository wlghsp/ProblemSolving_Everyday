
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(a, b):
    number_list = []
    number = 1
    while True:
        if len(number_list) >= b:
            break
        number_list += [number] * number
        number += 1
    return sum(number_list[a-1:b])

a, b = map(int, input().split())
print(solution(a, b))
