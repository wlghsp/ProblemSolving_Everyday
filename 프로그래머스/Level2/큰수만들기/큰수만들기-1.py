def solution(number, k):
    answer = [number[0]]
    for i in range(1, len(number)):
        while answer and answer[-1] < number[i] and k > 0:
            answer.pop()
            k -= 1
        answer.append(number[i])

    while k > 0:
        answer.pop()
        k -= 1
    return ''.join(map(str, answer))


print(solution("1924", 2)) # 94
print(solution("1231234", 3)) # 3234
print(solution("4177252841", 4)) # 775841
