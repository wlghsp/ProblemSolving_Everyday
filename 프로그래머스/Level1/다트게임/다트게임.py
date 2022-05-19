
'''
정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >> 이용
왼쪽(<<) 2배 늘어남 오른쪽(>>) 1/2로 줄어듬
'''

def solution(dartResult):
    sdt = ' SDT'
    ans = []
    idx = 0
    for i, c in enumerate(dartResult):
        if c in sdt:
            ans.append(int(dartResult[idx:i]) ** sdt.index(c))
        elif c == '#':
            ans[-1] = -ans[-1]
        elif c == '*':
            ans[-1] <<= 1
            if len(ans) >= 2:
                ans[-2] <<= 1

        if not c.isdecimal():
            idx = i + 1

    return sum(ans)


dartResult = "1S2D*3T"
print(solution(dartResult))
