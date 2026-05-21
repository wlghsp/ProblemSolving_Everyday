import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
def input(): return sys.stdin.readline().rstrip()

result = []
num = 1
while len(result) < 1_000_000:
    s = str(num)
    if len(s) == len(set(s)):
        result.append(num)
    num += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(result[n - 1])