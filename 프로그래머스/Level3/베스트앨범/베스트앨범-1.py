from collections import defaultdict


def solution(genres, plays):
    records = []
    genres_total = defaultdict(int)
    for i, (g, p) in enumerate(zip(genres, plays)):
        genres_total[g] += p
        records.append((g, p, i))

    # 장르 수 desc, 플레이수 desc, 인덱스 asc
    records.sort(key=lambda x: [(-genres_total[x[0]], -x[1], x[2])])

    answer = []
    genres_cnt = defaultdict(int)
    for g, p, i in records:
        if genres_cnt[g] < 2:
            answer.append(i)
            genres_cnt[g] += 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500])) # [4,1,3,0]
