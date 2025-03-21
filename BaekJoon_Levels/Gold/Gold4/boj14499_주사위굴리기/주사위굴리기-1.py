N, M, x, y, K = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 각 면 : [위, 아래, 앞, 뒤, 왼, 오]
TOP, BOTTOM, FRONT, BACK, LEFT, RIGHT = 0, 1, 2, 3, 4, 5
faces = [0] * 6


def roll_east():
    faces[LEFT], faces[TOP], faces[BOTTOM], faces[RIGHT] = \
        faces[BOTTOM], faces[LEFT], faces[RIGHT], faces[TOP]


def roll_west():
    faces[LEFT], faces[TOP], faces[BOTTOM], faces[RIGHT] = \
        faces[TOP], faces[RIGHT], faces[LEFT], faces[BOTTOM]


def roll_south():
    faces[FRONT], faces[TOP], faces[BACK], faces[BOTTOM] = \
        faces[BOTTOM], faces[FRONT], faces[TOP], faces[BACK]


def roll_north():
    faces[FRONT], faces[TOP], faces[BACK], faces[BOTTOM] = \
        faces[TOP], faces[BACK], faces[BOTTOM], faces[FRONT]


moves = {
    1: (0, 1, roll_east),
    2: (0, -1, roll_west),
    3: (-1, 0, roll_north),
    4: (1, 0, roll_south)
}

result = []
for c in commands:
    dx, dy, roll = moves[c]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M): continue

    roll()

    if mapp[nx][ny] == 0:
        mapp[nx][ny] = faces[BOTTOM]
    else:
        faces[BOTTOM] = mapp[nx][ny]
        mapp[nx][ny] = 0

    result.append(faces[TOP])
    x, y = nx, ny

print(*result, sep='\n')
