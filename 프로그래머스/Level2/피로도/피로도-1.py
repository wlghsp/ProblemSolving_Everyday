def solution(k, dungeons):
    len_dungeon = len(dungeons)
    combs = []
    def recur(picked):
        if len(picked) == len_dungeon:
            combs.append(picked[:])
            return
        for i in range(len_dungeon):
            if i in picked: continue
            picked.append(i)
            recur(picked)
            picked.pop()
    recur([])

    max_dungeon_cnt = 0
    for comb in combs:
        cur_piro = k
        dungeon_cnt = 0
        for c in comb:
            dungeon = dungeons[c]
            min_piro = dungeon[0]
            consume_piro = dungeon[1]
            if cur_piro >= min_piro:
                dungeon_cnt += 1
                cur_piro -= consume_piro
        max_dungeon_cnt = max(max_dungeon_cnt, dungeon_cnt)

    return max_dungeon_cnt

print(solution(80, [[80,20],[50,40],[30,10]])) # 3