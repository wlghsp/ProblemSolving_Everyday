import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
fibo_nums = [0] * (n+1)

if n == 0:
    print(0)
else:
    fibo_nums[0] = 0
    fibo_nums[1] = 1

    for i in range(2, n+1):
        fibo_nums[i] = fibo_nums[i-1] + fibo_nums[i-2]


    print(fibo_nums[n])

