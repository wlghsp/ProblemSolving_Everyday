name = input()

name_map = {}
for c in name:
    if c not in name_map:
        name_map[c] = 1
    else:
        name_map[c] += 1

front = ""
rear = ""
keys = sorted(name_map.keys()) # 사전순

for k in keys:
    while name_map[k] >= 2:
        front = front + k
        rear = k + rear
        name_map[k] -= 2

remainder = []
for k, v in name_map.items():
    if v > 0:
        remainder.append(k * v)

if len(remainder) >= 2:
    print("I'm Sorry Hansoo")
elif len(remainder) == 1:
    print(front + remainder[0] + rear)
elif len(remainder) == 0:
    print(front + rear)
