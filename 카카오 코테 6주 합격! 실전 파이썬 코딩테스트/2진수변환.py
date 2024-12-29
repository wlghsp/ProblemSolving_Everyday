# 2진수로 변환하기

def decimal_to_binary(k):
    if k == 1:
        return str(k)

    moks = k // 2

    smaller_output = decimal_to_binary(moks)

    cur_output = str(k % 2)

    return smaller_output + cur_output



example_deciaml = 11
res = decimal_to_binary(11)
print(res)