N, game_kind = input().split()
N = int(N)
names = set()
games = {'Y': 1, 'F': 2, 'O': 3}
for _ in range(N):
    names.add(input())

required = games[game_kind]
print(len(names) // required)
