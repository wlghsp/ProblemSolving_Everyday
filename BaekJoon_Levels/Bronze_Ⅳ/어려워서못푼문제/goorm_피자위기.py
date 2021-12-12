"""
20 7

23

100 5

124



"""

import sys
from typing import Counter

input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())


pizzas = n
pizzas += n // m
pizzas += ((n / m) + (n % m)) // m
print(int(pizzas))
