def solution(phone_book):
    # 한 번호가 다른 번호의 접두어라면 정렬한 상태에서 반드시 연속됨
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
            return False
    return True

print(solution(["119", "97674223", "1195524421"])) # false