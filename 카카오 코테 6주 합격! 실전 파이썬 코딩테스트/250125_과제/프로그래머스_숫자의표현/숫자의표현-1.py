def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        total = i
        for j in range(i + 1, n // 2 + 2): # 짝수는 절반 까지, 홀수는 절반 + 1 까지 확인
            total += j
            if total >= n:
                if total == n:
                    answer += 1
                break # break 를 해줘야 효율성 통과함
    return answer

print(solution(15)) # 4