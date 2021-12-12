"""
100
131

You are speeding and your fine is $500.

40
39

Congratulations, you are within the speed limit!


"""
import sys
input = lambda: sys.stdin.readline().rstrip()

speed_limit = int(input())
recorded_speed = int(input())

over_limit = recorded_speed - speed_limit

result = 0
if over_limit >= 31:
    result = 500
elif 21 <= over_limit <= 30:
    result = 270
elif 1 <= over_limit <= 20:
    result = 100
elif over_limit <= 0:
    result = 0

if result != 0:
    print(f"You are speeding and your fine is ${result}.")
else:
    print("Congratulations, you are within the speed limit!")
