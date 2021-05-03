s = [2, 2, 1, 3, 2]
d = 4
m = 2

# Complete the birthday function below.


def birthday(s, d, m):
    cnt = 0
    for i in range(0, n-m+1):
        if sum(s[i:i+m]) == d:
            cnt += 1
    return cnt


n = 5
print(birthday(s, d, m))
