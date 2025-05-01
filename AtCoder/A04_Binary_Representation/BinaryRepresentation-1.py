
N = int(input())

def to_binary(num):
    res = []
    while num != 0:
        res.append(str(num % 2))
        num //= 2
    return ''.join(reversed(res))

binary_num = to_binary(N)
print(binary_num.zfill(10))