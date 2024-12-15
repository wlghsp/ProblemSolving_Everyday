import sys
input = lambda : sys.stdin.readline().rstrip()


for _ in range(int(input())):
    a, b = input().split()
    a_sorted = sorted(list(a))
    b_sorted = sorted(list(b))

    if a_sorted == b_sorted:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
