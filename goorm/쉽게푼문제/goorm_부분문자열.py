import sys

input = lambda: sys.stdin.readline().rstrip()


input_string = input()


for i in range(1, len(input_string) + 1):
    print(input_string[:i])
