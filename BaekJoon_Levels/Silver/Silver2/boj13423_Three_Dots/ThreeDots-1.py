
for _ in range(int(input())):
    N = int(input())
    dots = list(map(int, input().split()))
    dots.sort()
    ans = 0
    for i in range(1, N - 1):

        left, right = 0, N - 1

        while left < i < right:
            a = dots[i] - dots[left]
            b = dots[right] - dots[i]

            if a == b:
                ans += 1
                left += 1
                right -= 1
            elif a > b:
                left += 1
            else:
                right -= 1
    print(ans)