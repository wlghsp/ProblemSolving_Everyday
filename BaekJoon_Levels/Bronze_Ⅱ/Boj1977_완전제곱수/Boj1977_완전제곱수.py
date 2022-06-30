
import sys
input = lambda : sys.stdin.readline().rstrip()

M = int(input())
N = int(input())

def isPerfectNum(num):
    # 제곱근을 정수로 바꿔서 다시 제곱했을 때 원래 수와 같으면 완전제곱수
    return int(num ** 0.5) ** 2 == num

nums = []
for i in range(M, N+1):
    if isPerfectNum(i):
        nums.append(i)

if len(nums) > 1:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)
