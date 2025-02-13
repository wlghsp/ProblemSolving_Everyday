def solution(n, lost, reserve):
    students = [1] * n
    for l in lost:
        students[l - 1] -= 1
    for r in reserve:
        students[r - 1] += 1

    for i, cnt in enumerate(students):
        if cnt == 0:
            if i - 1 >= 0 and students[i - 1] > 1:
                students[i - 1] -= 1
                students[i] += 1
            elif i + 1 < len(students) and students[i + 1] > 1:
                students[i + 1] -= 1
                students[i] += 1

    return len([i for i in students if i > 0])

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
