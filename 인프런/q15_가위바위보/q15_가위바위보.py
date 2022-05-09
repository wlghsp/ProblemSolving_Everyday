
N = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

for i in range(N):
    if a[i] == b[i]: print("D")
    elif a[i] == 2 and b[i] == 1: print("A")
    elif a[i] == 3 and b[i] == 2: print("A")
    elif a[i] == 1 and b[i] == 3: print("A")
    else: print("B")
