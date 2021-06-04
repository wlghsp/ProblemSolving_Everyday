

s, t = 7, 11
a, b = 5, 15
m, n = 3, 2
apples = [-2, 2, 1]
oranges = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleResult = 0
    orangeResult = 0
    for i in apples:
        position1 = i + a
        if position1 >= s and position1 <= t:
            appleResult += 1
    for i in oranges:
        position2 = i + b
        if position2 >= s and position2 <= t:
            orangeResult += 1
    print(appleResult, orangeResult, sep='\n')


countApplesAndOranges(s, t, a, b, apples, oranges)
