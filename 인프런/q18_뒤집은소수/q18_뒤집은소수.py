

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False

    return True


N = int(input())


nums = list(input().split())

for n in nums:
    reversed = int(n[::-1])
    if isPrime(reversed):
        print(reversed, end=' ')
