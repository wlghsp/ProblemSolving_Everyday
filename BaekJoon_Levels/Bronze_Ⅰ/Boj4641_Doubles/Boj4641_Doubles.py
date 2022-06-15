import sys

input = lambda: sys.stdin.readline().rstrip()

'''
2~15개의 서로 다른 자연수로 이루어진 리스트 
자신의 정확히 2배인 수가 있는 수의 개수

ex) 1 4 3 2 9 7 18 22, 2가 1의 2배, 4가 2의 2배, 18이 9의 2배 답은 3
'''

while True:
    nums = input()
    if nums == '-1':
        break
    nums = list(map(int, nums.split()))
    cnt = 0
    for n in nums:
        if n != 0 and (n * 2) in nums:
            cnt += 1
    print(cnt)
