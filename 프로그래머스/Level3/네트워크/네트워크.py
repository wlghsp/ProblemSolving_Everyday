
def solution(n, computers):
    answer = 0

    chk = [False] * (n)

    def dfs(i):
        for j in range(n):
            if computers[i][j] == 1 and not chk[j]:
                chk[j] = True
                dfs(j)

    for i in range(n):
        if not chk[i]:
            answer += 1
            chk[i] = True
            dfs(i)

    return answer

n = 3

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))