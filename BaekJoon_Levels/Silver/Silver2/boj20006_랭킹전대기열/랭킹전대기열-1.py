
P, M = map(int, input().split())
rooms = []
result = []

def check_if_matching_room(level):
    for room_level, players in rooms:
        if abs(room_level - level) <= 10 and len(players) < M:
            return True
    return False

for _ in range(P):
    level, nickname = input().split()
    level = int(level)
    if check_if_matching_room(level):
        found = False
        for room_level, players in rooms:
            if not found and abs(room_level - level) <= 10 and len(players) < M:
                players.append((level, nickname))
                found = True
    else:
        rooms.append((level, [(level, nickname)]))

for room_level, players in rooms:
    result.append("Waiting!" if len(players) < M else "Started!")
    players.sort(key=lambda x: x[1])
    for level, nickname in players:
        result.append(str(level) + " " + nickname)

print(*result, sep='\n')
