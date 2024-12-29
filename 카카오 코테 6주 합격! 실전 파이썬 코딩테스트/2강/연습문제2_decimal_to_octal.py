  # TODO: 10진수를 8진수로 변환하는 재귀 함수 작성
def decimal_to_octal(n):
    # 종료 조건
    if n == 0:
        return ""

    return decimal_to_octal(n // 8) + str(n % 8)


# 예시 출력
print(decimal_to_octal(10))  # 출력: 12
print(decimal_to_octal(64))  # 출력: 100