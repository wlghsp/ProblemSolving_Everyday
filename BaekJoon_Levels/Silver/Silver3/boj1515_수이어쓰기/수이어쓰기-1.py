number = input()

num = 0

while len(number) > 0:
    num += 1

    for n in list(str(num)):
        if number and n == number[0]:
            number = number[1:]

print(num)
