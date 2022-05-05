
def titleToNumber(columnTitle):
    answer = 0

    for c in columnTitle:
        answer = answer * 26 + ord(c) - 64

    return answer




print(titleToNumber("A")) # 1
print(titleToNumber("AB")) # 28
print(titleToNumber("ZY")) # 701
