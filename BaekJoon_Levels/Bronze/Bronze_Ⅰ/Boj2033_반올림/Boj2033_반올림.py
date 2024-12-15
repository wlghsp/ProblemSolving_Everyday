import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())

def roundUp(num):
    return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)

num = 10
while True:
    if N > num:
        N = roundUp(N / num) * num
    else:
        break
    num *= 10

print(N)


