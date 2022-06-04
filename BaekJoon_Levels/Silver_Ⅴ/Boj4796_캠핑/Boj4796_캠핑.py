
import sys
input = lambda : sys.stdin.readline().rstrip()
'''
P 일 중, L일동안 사용 가능
V일짜리 휴가 
최대 며칠동안 사용 가능?
'''
index = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    answer = ((v//p) * l) + min((v % p), l)
    print(f"Case {index}: {answer}")
    index += 1
