
N = int(input())

# 한수인지 확인
def is_hansu(number):
    if number < 100: # 1자리, 2자리 수는 전부 한수
        return True

    # 1000 보다 작거나 같으므로 3자리 숫자만 확인
    # 각자리 숫자 추출
    hun = number // 100
    ten = number % 100 // 10
    one = number % 10

    # 한수란? 자릿수 차이가 같은 숫자
    return True if (hun - ten) == (ten - one) else False

# 한수 카운트 함수
def count_hansu(number):
    count = 0

    for i in range(1, number + 1):
        if is_hansu(i):
            count += 1
    return count


print(count_hansu(N))