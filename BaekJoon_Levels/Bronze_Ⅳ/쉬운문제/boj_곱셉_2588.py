"""
472
385

2360
3776
1416
181720

"""
import sys

input = sys.stdin.readline

a = input()
b = input()

print(int(a) * int(b[2]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(int(a) * int(b))

