
def gcd_sub(a, b):
    while a * b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a + b

def gcd_mod(a, b):
    while a * b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
def gcd_rec(a, b): # a > b 라는 전제하에
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)

# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
a, b = map(int, input().split())

x, y, z = gcd_sub(a, b), gcd_mod(a ,b), gcd_rec(a ,b)
print(x, y, z)