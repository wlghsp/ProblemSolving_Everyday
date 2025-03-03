import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    min_dist = abs(x - r) + abs(y - c)
    # 맨해튼거리에서 k를 뺀 남은거리가 짝수가 아니거나, 거리가 k보다 크면 impossible
    if (k - min_dist) % 2 != 0 or min_dist > k:
        return answer

    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    dir_alpha = "dlru"
    dir = [(1, 0), (0, -1), (0, 1), (-1, 0)]

    answer = []
    def dfs(cx, cy, dist):
        if len(dist) >= k:
            if (cx, cy) == (r, c):
                answer.append("".join(dist))
                return
            return

        for i in range(4):
            nx, ny = cx + dir[i][0], cy + dir[i][1]
            if not (0 <= nx < n and 0 <= ny < m): continue

            if not answer:
                dfs(nx, ny, dist + [dir_alpha[i]])

    dfs(x, y, [])
    return answer[0]


print(solution(3, 4, 2, 3, 3, 1, 5))  # "dllrl"
