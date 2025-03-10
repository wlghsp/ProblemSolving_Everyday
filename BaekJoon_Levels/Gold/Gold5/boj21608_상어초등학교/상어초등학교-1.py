import heapq

N = int(input())
class_room = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N * N)]
student_map = {s[0]: set(s[1:]) for s in students}

for student, like1, like2, like3, like4 in students:
    spaces = []
    for x in range(N):
        for y in range(N):
            if class_room[x][y] != 0: continue
            blank_cnt = like_cnt = 0

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < N): continue

                if class_room[nx][ny] == 0:
                    blank_cnt += 1
                if class_room[nx][ny] in student_map[student]:
                    like_cnt += 1

            heapq.heappush(spaces, (-like_cnt, -blank_cnt, x, y))

    _, _, px, py = heapq.heappop(spaces)
    class_room[px][py] = student

result = 0
point = {4: 1000, 3: 100, 2: 10, 1: 1, 0: 0}
for i in range(N):
    for j in range(N):
        like_cnt = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = i + dx, j + dy
            if not (0 <= nx < N and 0 <= ny < N): continue

            if class_room[nx][ny] in student_map[class_room[i][j]]:
                like_cnt += 1
        result += point[like_cnt]

print(result)
