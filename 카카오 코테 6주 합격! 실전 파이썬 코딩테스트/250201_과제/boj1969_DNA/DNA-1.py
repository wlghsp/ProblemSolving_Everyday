
ACGT  = "ACGT"
acgt_map = {"A": 0, "C": 1, "G": 2, "T": 3}
N, M = map(int, input().split())
dnas = [input() for _ in range(N)]

s = ""
for i in range(M):
    atgc_cnt = [0] * 4
    for j in range(N):
        atgc_cnt[acgt_map[dnas[j][i]]] += 1
    max_val = atgc_cnt[0]
    max_idx = 0
    for j in range(4):
        if max_val < atgc_cnt[j]:
            max_val = atgc_cnt[j]
            max_idx = j
    s += ACGT[max_idx]

total = 0
for d in dnas:
    cnt = 0
    for i in range(M):
        if d[i] != s[i]:
            cnt += 1
    total += cnt
print(s, total, sep="\n")

