n = int(input())


i = 1


while i <= n:
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        print("X", end=" ")
    else:
        print(i, end=" ")
    i += 1


# print((a if a < b else b) if ((a if a < b else b) < c) else c)
