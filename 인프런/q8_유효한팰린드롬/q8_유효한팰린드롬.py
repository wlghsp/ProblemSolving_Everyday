



import re
str = input().upper()


str = re.sub('[^A-Z]', '', str)

print("YES") if str == str[::-1] else print("NO")