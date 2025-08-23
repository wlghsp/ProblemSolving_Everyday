def solution(lottos, win_nums):
    # 최고 순위와 최저 순위
    ranks = [6, 6, 5, 4, 3, 2, 1]
    common = len(set(lottos) & set(win_nums))
    zero_cnt = lottos.count(0)
    best = common + zero_cnt
    return [ranks[best], ranks[common]]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]	)) # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]		)) # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]			)) # [1, 1]