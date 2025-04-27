N = int(input())
A = list(map(int, input().split()))
A.sort()

found = False
for i in range(N):
    left = i + 1
    right = N - 1
    while left < right:
        total = A[i] + A[left] + A[right]
        if total == 1000:
            found = True
            break
        elif total < 1000:
            left += 1
        else:
            right -= 1

print("Yes" if found else "No")