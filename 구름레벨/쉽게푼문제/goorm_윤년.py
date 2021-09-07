

import sys

input = sys.stdin.readline


year = int(input())

print("Leap Year" if (year % 4 == 0 and year %
                      100 != 0) or year % 400 == 0 else "Not Leap Year")
