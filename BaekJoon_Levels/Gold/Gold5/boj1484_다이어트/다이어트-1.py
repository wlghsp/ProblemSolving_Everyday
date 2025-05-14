
G = int(input())

ans = []
left = 1

def get_diff(r, l):
    return r * r - l * l

for right in range(2, 100001):

    while left < right and (right * right - left * left) > G:
        left += 1

    if (right * right - left * left) == G:
        ans.append(right)
if not ans:
    print(-1)
else:
    print(*ans, sep='\n')