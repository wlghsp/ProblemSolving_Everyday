def recur(str):
    if len(str) == 1:
        return str

    return recur(str[:len(str) // 3]) + " " * (len(str) // 3) + recur(str[-len(str) // 3:])

while True:
    try:
        n = int(input())
        print(recur("-" * (3 ** n)))

    except EOFError:
        break