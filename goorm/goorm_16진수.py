import sys

input = sys.stdin.readline


n = int(input())
print(hex(n)[2:])

"""
2진수 bin()
8진수 oct()
16진수 hex()
앞의 진법표시를 지울려면 [2:]을 붙인다. 

"""
