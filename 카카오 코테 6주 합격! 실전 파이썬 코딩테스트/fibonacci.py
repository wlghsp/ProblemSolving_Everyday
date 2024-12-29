# 피보나치 수열 구현

def fibonacci(n):
    n = n - 1

    if n >= 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)

N = int(input("자연수를 입력하세요: "))
print(f'피보나치 수열의 {N}번째 항 = {fibonacci(N)}')

'''
1. 종료조건 2. 재귀호출 + 데이터 통합   
'''