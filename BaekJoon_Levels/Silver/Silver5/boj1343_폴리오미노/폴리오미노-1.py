
board = input()

for polio in ["AAAA", "BB"]:
    board = board.replace("X" * len(polio), polio)


print(-1 if "X" in board else board)