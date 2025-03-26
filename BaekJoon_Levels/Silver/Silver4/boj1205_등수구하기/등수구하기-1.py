
N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    # 점수의 갯수와 랭킹리스트의 갯수가 같으며, 가장 낮은 점수가 새 점수 이상이면
    if N == P and scores[-1] >= new_score:
        print(-1)
    else:
        rank = N + 1 # 새 점수가 원래 점수들 보다 낮은 경우 대비해 마지막 등수로 초기화
        for i in range(N):
            if scores[i] <= new_score:
                rank = i + 1
                break
        print(rank)