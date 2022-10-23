


def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer

def solution1(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)



print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4
