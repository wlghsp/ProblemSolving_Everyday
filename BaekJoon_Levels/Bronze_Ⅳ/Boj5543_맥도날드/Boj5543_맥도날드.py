import sys
input = lambda : sys.stdin.readline().rstrip()

burgers = []
for _ in range(3):
    burgers.append(int(input()))

drink = []
for _ in range(2):
    drink.append(int(input()))

min_burger = min(burgers)
min_drink = min(drink)

print(min_burger + min_drink - 50)