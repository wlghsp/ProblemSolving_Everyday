"""
삼각형 외우기 

60
70
50

Scalene
"""
import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

sum_of_angles = a + b + c


def triangle_remember(a, b, c):
    result = ""
    if sum_of_angles == 180:
        if a == b == c:
            result = "Equilateral"
        elif a == b or a == c or b == c:
            result = "Isosceles"
        elif a != b and a != c and b != c:
            result = "Scalene"
    else:
        result = "Error"

    return result


print(triangle_remember(a, b, c))


