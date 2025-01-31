import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
corridor = [list(input().split()) for _ in range(N)]
# 빈 공간 조합을 만들어 벽을 설치하기 위해 빈 공간 좌표 리스트
empty_spaces = []
# 벽을 설치하고 선생님들에서 탐색을 시작하여 감시 피할 수 있는지 여부 확인
teachers = []


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 빈 공간 및 선생님 위치 저장
for i in range(N):
    for j in range(N):
        if corridor[i][j] == 'X':
            empty_spaces.append((i, j))
        elif corridor[i][j] == 'T':
            teachers.append((i, j))

# 감시를 피할 수 있는지 검사
def can_avoid_detection():
    for x, y in teachers:

        for i in range(4): # 4방향 검사
            nx, ny = x, y
            while True:
                # 해당 방향으로 계속 전진
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N: break # 범위 밖이면 멈춤
                if corridor[nx][ny] == 'O': break # 벽 만나면 멈춤
                if corridor[nx][ny] == 'S': return False # 학생 발견이면 False 반환 감시 못 피함
    return True # 모든 감시를 피할 수 있음


def place_walls(count, start):
    if count == 3: # 벽 3개 설치 완료
        if can_avoid_detection():
            print("YES")
            exit()
        return

    for i in range(start, len(empty_spaces)):
        r, c = empty_spaces[i][0], empty_spaces[i][1]

        corridor[r][c] = 'O' # 벽 설치
        place_walls(count + 1, i + 1)
        corridor[r][c] = 'X' # 백트래킹 (벽 제거)

place_walls(0, 0) # count = 0 에서 시작

print("NO")