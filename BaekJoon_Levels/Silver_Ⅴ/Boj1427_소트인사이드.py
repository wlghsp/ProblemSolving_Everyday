

import sys

input = lambda : sys.stdin.readline().rstrip()


nums = [int(i) for i in list(input())]
nums.sort(reverse=True)
print(''.join(list(map(str, nums))))

# 2143