def solution(sequence, k):
    answer = []
    left = 0
    total = 0
    for right in range(len(sequence)):
        total += sequence[right]
        while total > k:
            total -= sequence[left]
            left += 1
        if total == k:
            answer.append([right - left + 1, left, right])
    answer.sort(key= lambda x: [x[0], x[1]])

    return [answer[0][1], answer[0][2]]

print(solution([1, 2, 3, 4, 5], 7))

