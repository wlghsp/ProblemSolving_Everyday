
def intToRoman(num):
    codeInt = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    stringRoman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    answer = ""
    for i in range(len(codeInt)):
        while num >= codeInt[i]:
            answer += stringRoman[i]
            num -= codeInt[i]
    return answer



