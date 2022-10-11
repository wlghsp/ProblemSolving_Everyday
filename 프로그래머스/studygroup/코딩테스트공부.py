def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    time = 0
    for a, b, c, d, e in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)
        time += e
    #  목표 알고력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    # dp[초기 알고력][초기 코딩력] = 0으로 기저 사례를 잡고
    # 나머지 DP 배열의 값은 무한(적당히 큰 값)으로 초기화
    INF = float('inf')
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp: # 도달해야할 알고력보다 작거나 같을 때
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1) #
            if j + 1 <= max_cop: # 도달해야할 코딩력보다 작거나 같을 때
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            # 풀 수 있는 문제 풀어서 알고력, 코딩력을 높인다.
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req: # 알고력과 코딩력이 풀이에 필요한 것보다 높아서 풀 수 있을 때
                    next_alp, next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[-1][-1]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))  # 15
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))  # 13
