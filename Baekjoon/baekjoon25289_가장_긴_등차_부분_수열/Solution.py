import sys
input = sys.stdin.readline

def solve():
    pass

def solve_test(n, a):
    dp = [{} for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            diff = a[j] - a[i]
            dp[j][diff] = dp[i].get(diff, 1) + 1
    max_diff = 0
    for d in dp:
        if d.values():
            max_diff = max (max_diff, max(d.values()))
    return max_diff

if __name__ == "__main__":
    # 예제 1: 8 / 1 2 3 6 5 3 7 9 → 5 (1,2,3,5,7 or 3,5,7,9... 확인 필요)
    # 예제 2: 5 / 5 4 3 2 1 → 5

    tests = [
        (8, [1, 2, 3, 6, 5, 3, 7, 9]),  # Expected: 5
        (5, [5, 4, 3, 2, 1]),            # Expected: 5
    ]

    for n, a in tests:
        print(solve_test(n, a))



    
    
