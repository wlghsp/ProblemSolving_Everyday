import string
import math

def solution(n, k):
    answer = 0
    # 1. k 진수 변환
    temp = string.digits
    def convert(num, base):
        if num == 0:
            return '0'
        res = ''
        while num != 0:
            num, mod = divmod(num, base)
            res = temp[mod] + res
        return res
    S = convert(n, k)

    def is_prime(num):
        if '0' in num:
            return False
        num = int(num)
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if  num % i == 0:
                return False
        return True


    def does_condition_matched(start, end):
        #  1. 0P0처럼 소수 양쪽에 0이 있는 경우
        if (start - 1 >= 0 and end + 1 < len(S)) and S[start - 1] == '0' and S[end + 1] == '0' and is_prime(S[start:end + 1]):
            return True
        # 2. P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무 것도 없는 경우
        elif start == 0 and (end + 1 < len(S) and S[end + 1] == '0') and is_prime(S[start:end + 1]):
            return True
        # 3. 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무 것도 없는 경우:
        elif end == len(S) - 1 and (start - 1 >= 0 and S[start - 1] == '0') and is_prime(S[start:end + 1]):
            return True
        #  4. P처럼 소수 양쪽에 아무 것도 없는 경우
        elif (start - 1 < 0 and end + 1 >= len(S)) and is_prime(S[start:end + 1]):
            return True

        return False


    # 2. 탐색하여 조건에 맞는 소수 찾아 갯수 리턴
    for i in range(len(S)):
        for j in range(i, len(S)):
            if does_condition_matched(i, j):
                answer += 1

    return answer


print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2