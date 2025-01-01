

N = int(input())


for _ in range(N):
    ps = input()
    stk = []

    is_valid = True
    for p in ps:
        if p == '(':
            stk.append(p)
        elif p == ')':
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            else:
                is_valid = False
                break

    if is_valid and len(stk) == 0:
        print("YES")
    else:
        print("NO")
