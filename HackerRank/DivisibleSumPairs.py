

def divisibleSumPairs(n, k, ar):
    # Write your code here
    cnt = 0
    length = len(ar)
    for i in range(length):
        for j in range(i+1, length):
            if (ar[i] + ar[j]) % k == 0:
                cnt += 1
    return cnt


ar = [1, 2, 3, 4, 5, 6]
n = len(ar)
k = 5

print(divisibleSumPairs(n, k, ar))
