def solution(answers):
    res = [0] * 3
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    max_cnt = 0
    for j in range(len(students)):
        for i in range(len(answers)):
            if answers[i] == students[j][i % len(students[j])]:
                res[j] += 1
        if max_cnt < res[j]:
            max_cnt = res[j]

    # 최댓값 학생 담기
    ans = []
    for i in range(len(res)):
        if max_cnt == res[i]:
            ans.append(i + 1)
    return ans


print(solution([1,3,2,4,2]))  # [1, 2, 3]
