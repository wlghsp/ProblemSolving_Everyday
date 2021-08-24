"""
ord(문자) 아스키코드를 반환한다. 
chr(숫자) 숫자에 맞는 아스키코드를 반환한다. 
"""

import sys

input = sys.stdin.readline

n = input().rstrip()
print(ord(n))
