def recur(n):
    print(n)
    if n != 1:
        recur(n - 1)


n = int(input())

recur(n)
