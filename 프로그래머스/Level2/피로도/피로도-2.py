def solution(k, dungeons):
    len_dungeons = len(dungeons)
    max_dungeon_cnt = 0
    def recur(picked, visited, cur_piro, dungeon_cnt):
        nonlocal max_dungeon_cnt
        max_dungeon_cnt = max(max_dungeon_cnt, dungeon_cnt)

        for i in range(len_dungeons):
            if visited[i]: continue
            min_piro, consume_piro = dungeons[i]
            if cur_piro >= min_piro:
                visited[i] = True
                recur(picked + [i], visited, cur_piro - consume_piro, dungeon_cnt + 1)
                visited[i] = False

    recur([], [False] * len_dungeons, k, 0)
    return max_dungeon_cnt


print(solution(80, [[80,20],[50,40],[30,10]])) # 3