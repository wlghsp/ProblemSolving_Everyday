import sys
input = lambda : sys.stdin.readline().rstrip()


books = dict()

for _ in range(int(input())):
    x = input()
    if x in books:
        books[x] += 1
    else:
        books[x] = 1

max_val = max(books.values())

arr = []

for k, v in books.items():
    if v == max_val:
        arr.append(k)

arr.sort()

print(arr[0])