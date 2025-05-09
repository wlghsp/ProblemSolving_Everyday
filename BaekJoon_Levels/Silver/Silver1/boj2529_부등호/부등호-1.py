
K = int(input())
signs = list(input().split())

min_str, max_str = '', ''
min_val, max_val = float('inf'), -1

def by_sign(sign, a, b):
    if sign == '>':
        return a > b
    return a < b

def recur(picked):
    global min_str, max_str, min_val, max_val
    if len(picked) == (K + 1):
        res = ''.join(map(str, picked))
        num_res = int(res)
        if num_res < min_val:
            min_val = num_res
            min_str = res
        if num_res > max_val:
            max_val = num_res
            max_str = res
        return

    for i in range(10):
        if i in picked: continue
        if picked and not by_sign(signs[len(picked) - 1], picked[-1], i): continue

        picked.append(i)
        recur(picked)
        picked.pop()


recur([])


print(max_str)
print(min_str)

