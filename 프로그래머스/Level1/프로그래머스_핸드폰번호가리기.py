def solution(phone_number):
    return "*" * len(phone_number[:-4]) + phone_number[-4:]


phone = "027778888"

print(solution(phone))
