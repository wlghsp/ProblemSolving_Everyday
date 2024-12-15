import sys
input = lambda : sys.stdin.readline().rstrip()

w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w.sort(reverse=True)
k.sort(reverse=True)

w_score = sum(w[:3])
k_score = sum(k[:3])

print(w_score, k_score)
