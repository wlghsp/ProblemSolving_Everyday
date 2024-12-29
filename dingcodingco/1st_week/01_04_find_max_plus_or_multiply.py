def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum_of_calc = 0
    for num in array:
        if num <= 1 or sum_of_calc <= 1:
            sum_of_calc += num
        else:
            sum_of_calc *= num

    return sum_of_calc


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))