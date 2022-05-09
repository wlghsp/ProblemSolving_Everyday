


str = input()


answer = ""
for s in list(str):
    if s.isupper():
        answer += s.lower()
    elif s.islower():
        answer += s.upper()

print(answer)