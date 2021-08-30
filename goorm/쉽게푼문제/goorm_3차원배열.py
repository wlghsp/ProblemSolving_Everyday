array = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24, 25, 26, 27],
]


for a in array:
    for i in a:
        print(i, end=" ")
        if i % 3 == 0:
            print()
    print()
