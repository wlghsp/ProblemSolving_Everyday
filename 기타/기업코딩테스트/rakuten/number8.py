

def sort_list(a):
    i = 0
    while i < len(answer):
        key = i
        j = i + 1
        while j < len(a):
            if a[key] > a [j]:
                key = j
            j += 1
        a[i], a[key] = a[key], a[i]
        i += 1
    return a
items = [3, 1, 2]
answer = [(i,j) for j in items for i in items]
sort_list(answer)
k = 7

print(answer)



