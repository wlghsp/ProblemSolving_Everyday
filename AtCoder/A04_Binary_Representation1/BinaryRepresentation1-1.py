
N = int(input())

def to_binary(num):
    res = []
    for x in range(9, -1, -1):
        wari = 1 << x # 2 의 x 제곱
        res.append(str((num // wari) % 2))
    return ''.join(res)

binary_num = to_binary(N)
print(binary_num)