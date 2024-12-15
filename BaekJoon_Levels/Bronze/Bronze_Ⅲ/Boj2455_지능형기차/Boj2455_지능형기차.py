import sys
input = lambda : sys.stdin.readline().rstrip()

'''
기차 안에 사람이 가장 많을 때의 사람 수 
'''
people = 0
nums = []
for _ in range(4):
    off, on = map(int, input().split())
    people += on - off
    nums += [people]
print(max(nums))
