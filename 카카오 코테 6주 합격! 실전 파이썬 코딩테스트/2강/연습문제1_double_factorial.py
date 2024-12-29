
# TODO: 더블 팩토리얼을 계산하는 재귀 함수 작성
def double_factorial(n):
    # 종료 조건
    if n <= 0:
        return 1
    return n * double_factorial(n - 2)

# 예시 출력
print(double_factorial(5))  # 출력: 15
print(double_factorial(6))  # 출력: 48