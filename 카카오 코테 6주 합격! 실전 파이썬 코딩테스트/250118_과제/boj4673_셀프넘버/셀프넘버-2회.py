


def self_number(num):
    result = num
    while num != 0:
        result += num % 10
        num //= 10
    return result

self_nums = set()
for i in range(1,10001):
    self_nums.add(self_number(i))

for i in range(1, 10001):
    if i not in self_nums:
        print(i)