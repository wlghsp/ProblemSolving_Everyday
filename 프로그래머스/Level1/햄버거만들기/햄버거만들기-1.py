def solution(ingredient):
    answer = 0
    stk = []
    for ing in ingredient:
       stk.append(ing)
       if len(stk) >= 4 and (stk[-1] == 1 and stk[-2] == 3 and stk[-3] == 2 and stk[-4] == 1):
           answer += 1
           for _ in range(4):
               stk.pop()

    return answer

print(solution(
[2, 1, 1, 2, 3, 1, 2, 3, 1]
)) # 2