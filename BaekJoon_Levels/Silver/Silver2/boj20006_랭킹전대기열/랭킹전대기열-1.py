def check_if_matching_room(level, M, rooms):
    for room_level, v in rooms.items():
        if abs(room_level - level) <= 10 and len(v) < M:
            return True

    return False


P, M = map(int, input().split())
rooms = {}
result = []

for _ in range(P):
    level, nickname = input().split()
    level = int(level)
    if len(rooms) > 0 and check_if_matching_room(level, M, rooms):
        found = False
        for room_level, v in rooms.items():
            if not found and abs(room_level - level) <= 10 and len(v) < M:
                v.append((level, nickname))
                found = True
                rooms[room_level] = v
    else:
        rooms[int(level)] = [(level, nickname)]

for v in rooms.values():
    result.append("Waiting!" if len(v) < M else "Started!")
    v.sort(key=lambda x: x[1])
    for level, nickname in v:
        result.append(str(level) + " " + nickname)

print(*result, sep='\n')
