def solution(n, t, m, p):
    number = 0

    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # n진수를 10진수로 변환하는 함수
    def convert(num, base):
        if num == 0:
            return '0'
        res = ''
        while num > 0:
            num, mod = divmod(num, base)
            res = tmp[mod] + res
        return res
    total = []
    while len(total) < (t * m):
        total.append(convert(number, n))
        number += 1
    total = ''.join(total)[:t * m]
    answer = []
    for i in range(p - 1, t * m, m):
        answer.append(total[i])
    return ''.join(answer)


print(solution(2, 4, 2, 1))  # "0111"
print(solution(16, 16, 2, 1))  # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
