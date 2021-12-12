




def stoi(s, n):
    ret = 0
    l = len(s)
    for i in range(l): ret += int(s[i]) * n**(l-i-1)
    return ret

def stoi1(s, n):
    ret = 0
    for i in s:
        ret = ret * n + int(i)
    return ret