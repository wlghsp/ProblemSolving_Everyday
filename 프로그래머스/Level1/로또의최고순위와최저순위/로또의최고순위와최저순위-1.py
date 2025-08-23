def solution(lottos, win_nums):
    ranks = {cnt: rank for cnt, rank in zip(range(6, 1, -1), range(1, 6))}
    ranks[0] = 6
    ranks[1] = 6
    min_cnt = len(set(lottos) & set(win_nums))
    zero_cnt = lottos.count(0)
    max_cnt = min(zero_cnt, 6 - min_cnt) + min_cnt
    return [ranks[max_cnt], ranks[min_cnt]]

# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3,5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # 	[1, 6]
print(solution(	[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # 	[1, 1]