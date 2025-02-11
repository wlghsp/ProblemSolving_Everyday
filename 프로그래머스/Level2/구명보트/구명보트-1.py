def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit: # 무게 제한 이하라면 둘다 태움
            i += 1
            j -= 1
        else: # 무게 제한 이상이라면 무거운 사람만 태움
            j -= 1

        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100)) # 3