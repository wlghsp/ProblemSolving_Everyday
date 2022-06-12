
def solution(p):
    answer = [0] * len(p)
    i = 0
    sorted_p = sorted(p)
    while True:
        j = p.index(min(p[i:]))
        if i != j:
            p[i], p[j] = p[j], p[i]
            answer[i] += 1
            answer[j] += 1
        if sorted_p == p:
            break
        i += 1

    return answer



print(solution([2,5,3,1,4])) # 1 1 0 3 1
print(solution([2,3,4,5,6,1])) # 1 1 1 1 1 5