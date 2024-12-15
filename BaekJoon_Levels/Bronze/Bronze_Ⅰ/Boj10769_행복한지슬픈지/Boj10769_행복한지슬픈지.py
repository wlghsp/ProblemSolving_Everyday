import sys
input = lambda : sys.stdin.readline().rstrip()

sen = input()
list = []
happy = sen.count(":-)")
sad = sen.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
