
n = int(input())

end = 1
level = 1
while n > end:
    end += 6 * level
    level += 1
print(level)

"""

O(루트N)시간 복잡도
1억까지이므로, 31,622 회 정도 연산
"""