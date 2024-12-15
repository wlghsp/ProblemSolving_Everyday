import sys

input = lambda: sys.stdin.readline().rstrip()


while True:
    nums = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, n//2 + 1):
        if n % i == 0:
            nums.append(i)
    if n == sum(nums):
        print(n, end=' = ')
        for i in nums[:len(nums)-1]:
            print(i, end=' + ')
        print(nums[-1])
    else:
        print(f"{n} is NOT perfect.")

