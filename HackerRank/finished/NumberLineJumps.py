
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1 != v2 and (x2-x1) % (v2-v1) == 0:
            return 'YES'
        else:
            return 'NO'


x1 = 0
v1 = 3
x2 = 4
v2 = 2
result = kangaroo(x1, v1, x2, v2)

print(result)
