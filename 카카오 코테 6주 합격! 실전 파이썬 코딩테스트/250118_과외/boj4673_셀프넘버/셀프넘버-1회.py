def generate_number(n): #
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result


MAX_NUM = 10000

numbers = set()
for i in range(1, MAX_NUM + 1):
    numbers.add(generate_number(i)) # 생성자가 있는 숫자들

for i in range(1, MAX_NUM + 1):
    if i not in numbers:
        print(i)

