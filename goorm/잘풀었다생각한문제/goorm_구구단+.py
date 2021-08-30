import sys

input = lambda: sys.stdin.readline().rstrip()


n = int(input())


for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end=" ")  # 한줄로 출력 됨.
        if j % n == 0: 
            print()
