# 2진수로 변환하기

def decimal_to_binary(k):
    # 종료 조건
    if k == 0:
        return ""

    return decimal_to_binary(k // 2) + str(k % 2)


example_deciaml = 11
res = decimal_to_binary(11) # 1011
print(res)