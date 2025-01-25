

def d(n):
    result = n
    while n != 0:
        result += n % 10
        n //= 10
    return result

not_self_nums = set()
for i in range(1, 10001):
    not_self_nums.add(d(i))

for i in range(1, 10001):
    if i not in not_self_nums:
        print(i)