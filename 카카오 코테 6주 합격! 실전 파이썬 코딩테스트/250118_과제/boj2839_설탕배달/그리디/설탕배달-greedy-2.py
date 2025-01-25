

N = int(input())

def sugar(n):
    cnt = 0
    while n >= 0:
        if n % 5 == 0:
            cnt += n // 5
            return cnt

        n -= 3
        cnt += 1
    return -1

print(sugar(N))