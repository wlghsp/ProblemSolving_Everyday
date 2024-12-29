

def flatten(l):
    if not isinstance(l, list):
        return [l]

    res = []

    for item in l:
        res += flatten(item)

    return res

print(flatten([1, [2, 3, 4], [5, 6, [7, 8]]]))