import sys
input = sys.stdin.readline


a, b = input().split()
a = int(a)
b = int(b)
if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")
