def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            num += 1
            answer.append(num)
        else:
            s = '0' + bin(num)[2:]
            # 홀수에서는 오른쪽에서 01 을 찾아 10으로 변경하는 것이 2개 이하 변경하면서 최소 증가
            i = s.rfind('01')
            s = list(s)
            s[i], s[i + 1] = '1', '0'
            answer.append(int(''.join(s),2))

    return answer


print(solution([2, 7])) # [3, 11]