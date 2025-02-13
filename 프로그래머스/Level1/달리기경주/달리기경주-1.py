def solution(players, callings):
    player_rank = {name: i for i, name in enumerate(players)}

    for outrun_player in callings:
        outrun_rank = player_rank[outrun_player]
        front_rank = outrun_rank - 1
        front_player = players[front_rank]

        player_rank[front_player] = outrun_rank
        player_rank[outrun_player] = front_rank
        players[outrun_rank] = front_player
        players[front_rank] = outrun_player

    return players


print(solution(
["mumu", "soe", "poe", "kai", "mine"],
["kai", "kai", "mine", "mine"]
)) # ["mumu", "kai", "mine", "soe", "poe"]