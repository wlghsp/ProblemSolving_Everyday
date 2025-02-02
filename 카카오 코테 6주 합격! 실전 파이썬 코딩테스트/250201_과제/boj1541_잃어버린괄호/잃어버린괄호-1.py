expression = input()
operators = []
result = 0
num = ""
minus_found = False
for i in range(len(expression)):
    c = expression[i]
    if c.isdigit():
        num += c
    else:
        if minus_found:
            result -= int(num)
        else:
            result += int(num)

        if c == "-":
            minus_found = True

        num = ""

    if i == len(expression) - 1:
        if minus_found:
            result -= int(num)
        else:
            result += int(num)


print(result)