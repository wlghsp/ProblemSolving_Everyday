import sys
input = lambda : sys.stdin.readline().rstrip()

nums = [i for i in map(int, input().split())]

minVal = min(nums)

while True:
    cnt = 0
    for i in range(5):
        if minVal % nums[i] == 0:
            cnt += 1
    if cnt > 2:
        print(minVal)
        break
    minVal += 1

'''
자연수 중에서 최솟값 부터 시작해서 나누어지는 수가 3개 이상인 수를 찾는다.
계속 1씩 증가시킨다. 
'''