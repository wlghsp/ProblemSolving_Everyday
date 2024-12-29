# TODO: 유클리드 호제법을 이용한 GCD 함수 작성
def gcd(a, b):
    # 종료 조건
    if a % b == 0:
        return b

    return gcd(b, a % b)


# 예시 출력
print(gcd(48, 18))  # 출력: 6
print(gcd(56, 42))  # 출력: 14
