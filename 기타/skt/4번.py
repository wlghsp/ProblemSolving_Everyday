"""
평지 혹은 숲으로 이동 가능
야영은 오직 평지에서만 가능
야영을 할 경우 다음날 다시 최대 K 칸 이동 가능
야영을 하지 않으면 다음날 이동 불가
. 은 평지, F는 숲, # 은 강


"""
from collections import deque
def solution(grid, k):
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n = (len(grid))
    m = (len(grid[0]))
    queue = deque()
    for i in range(len(grid)):
        grid[i] = list(grid[i].split())

    def bfs():
        global answer
        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == m-1:
                print("success")
                return
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if (grid[nx][ny] == '.' or grid[nx][ny] == 'F') and grid[x][y] < k:
                        grid[nx][ny] = grid[x][y] + 1
                        queue.append((nx, ny))
                        continue
                    elif grid[nx][ny] == '.' and grid[x][y] >= k:
                        grid[nx][ny] = 0
                        answer += 1
                        queue.append((nx, ny))

    queue.append((0,0))
    grid[0][0] = 0
    bfs()


    return answer


print(solution(["..FF", "###F", "###."], 4))  # 1
# print(solution(["..FF", "###F", "###."], 5))  # 0
# print(solution([".F.FFFFF.F", ".########.", ".########F", "...######F",
#                 "##.######F", "...######F", ".########F", ".########.",
#                 ".#...####F", "...#......"], 6))  # 3
