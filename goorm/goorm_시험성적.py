# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
scores = list(map(int, input().split()))
goorm_average = round(sum(scores) / len(scores), 2)

level = ""
if goorm_average >= 90:
    level = "A"
elif goorm_average >= 80:
    level = "B"
elif goorm_average >= 70:
    level = "C"
elif goorm_average >= 60:
    level = "D"
elif goorm_average < 60:
    level = "F"

print("{:.2f}".format(goorm_average), end=" ")
print(level)    
