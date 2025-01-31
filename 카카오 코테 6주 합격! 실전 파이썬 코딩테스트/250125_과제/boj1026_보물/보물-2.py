
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

used = [False] * (N + 1)
min_sum = 0
for i in range(N):
    max_val = -1
    max_idx = -1
    for j in range(N):
        if not used[j] and B[j] > max_val:
            max_val = B[j]
            max_idx = j
    min_sum += A[i] * B[max_idx]
    used[max_idx] = True

print(min_sum)
'''
1. 명제: 두 배열에서 한 배열의 오름차순 순서, 다른 배열은 내림차순 순서로 원소를 곱해서 더하면 합이 최솟값
2. 가정: 두 배열에서 한 배열의 오름차순 순서, 다른 배열은 내림차순 순서로 원소를 곱하지 않아도 합이 최솟값
3. 모순:

가정대로 계산
A = [1, 1, 3]
B = [10, 30, 20]

1 * 10 + 30 * 1 + 3 * 20 = 100

정렬하여 계산
A = [1, 1, 3]
B = [10, 20, 30]
10 * 3 + 20 * 1 + 30 * 1 = 80

더 작은 값이 존재하여 가정은 모순이므로 명제는 참이다.

'''
