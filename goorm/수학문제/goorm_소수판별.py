"""
 소수는 자기자신과 1이외에는 어떠한 정수라도 나뉘어 떨어지지 않는 수
 약수가 1과 자기자신 2개뿐
 2부터 n-1까지 어떤 정수로도 나뉘어지지 않아야 함.

"""
import sys
import math

input = lambda: sys.stdin.readline().rstrip()


def isPrimenum(num):

    # 비효율적인 코드
    # for i in range(2, num):
    #     if num % i == 0:
    #         return False

    """
    소수가 될 가능성을 가진 수는 그 수의 약수들이며
    그 약수들은 대칭적으로 그 수를 만든다. 
    따라서 그 약수의 가운데 약수 다시말하면 제곱급까지만 확인하면 된다. 
    """
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


num = int(input())

print(isPrimenum(num))
