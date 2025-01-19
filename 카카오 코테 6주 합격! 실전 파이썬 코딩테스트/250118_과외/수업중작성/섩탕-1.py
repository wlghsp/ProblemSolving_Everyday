
N = int(input())

def rec(n, cnt):
    if n == N:
        return cnt
    if n > N:
        return float('inf')

    result = min(rec(n + 5, cnt + 1), rec(n + 3, cnt + 1))

    return result

result = rec(0, 0)
if result == float('inf'):
    print(-1)
else:
    print(result)
