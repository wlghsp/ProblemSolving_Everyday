def recur(k):
    if k == 0:
        print("-", end="")
        return

    recur(k - 1)
    print(' ' * (3 ** (k - 1)), end="")
    recur(k - 1)



while True:
    try:
        n = int(input())
        recur(n)
        print()
    except:
        break