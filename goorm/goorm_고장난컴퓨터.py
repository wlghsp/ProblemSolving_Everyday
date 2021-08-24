"""
n 혜지가 입력한 글자의 수
c 코드가 지워지지 않고 유지되는 시간

각 글자를 입력할 때 코딩을 시작한 시점부터의 경과시간 

6 5
1 3 8 14 19 20

3 

"""


def numOfLetter(n, c):
    times = list(map(int, input().split()))
    result = 1  # 제한시간이 지났어도 입력한 숫자로 인해 최소한 한 개의 문자는 남는다.
    for i in range(len(times)-1):  # -1을 하여 마지막 인덱스를 초과하지 않게 한다.
        if times[i+1] - times[i] > c:
            result = 1
        else:
            result += 1
    return result


n, c = map(int, input().split())
times = []
print(numOfLetter(n, c))
