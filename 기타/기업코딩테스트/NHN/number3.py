
from collections import deque



def solution(maze, queries):
    answer = []
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    def is_valid_coord(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])
    def bfs(x, y, goalX, goalY, move_ok, d):
        queue = deque([(x, y, d)])
        visited[x][y] = True
        minVal = float("inf")
        flag = False
        while queue:
            x, y, d = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = d + 1
                if not is_valid_coord(nx,ny): continue
                if (nx) == goalX and (ny) == goalY:
                    flag = True
                    minVal = min(minVal, nd)
                if maze[nx][ny] in move_ok and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, nd))
        if not flag: return -1
        return minVal

    for query in queries:
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        que = list(query.split())
        val = bfs(int(que[0])-1,int(que[1])-1, int(que[2])-1, int(que[3]) -1, que[4], 1)
        answer.append(val)
    return answer


maze1 = ["AAAAA", "AABBB", "CAEFG", "AAEFF"]
queries1 = ["1 1 1 5 AF", "1 1 4 5 AF", "2 1 4 5 FAE", "1 5 4 5 ABF", "1 1 4 1 A"]
print(solution(maze1, queries1))
# maze2 = ["AAA", "ABB", "ABA"]
# queries2 = ["1 1 1 3 A", "1 3 3 1 A", "1 1 3 3 A", "1 1 3 3 AB"]
# print(solution(maze2, queries2))