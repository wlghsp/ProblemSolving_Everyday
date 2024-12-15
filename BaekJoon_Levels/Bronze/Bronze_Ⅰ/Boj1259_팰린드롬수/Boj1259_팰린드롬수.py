import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    a = input()
    if a == "0":
        break
    print("yes" if a == a[::-1] else "no")
