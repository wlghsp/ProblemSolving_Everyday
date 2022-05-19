
# https://youtu.be/4-iyppqNCyg

# Loop를 활용한 솔루션 : 시간초과 뜸.
def solution_Loop(phone_book):
    # 1. 비교할 A 선택
    for i in range(len(phone_book)):
    # 2. 비교할 B 선택
       for j in range(i+1, len(phone_book)):
    # 3. 서로가 서로의 접두어인지 확인한다.
           if phone_book[i].startswith(phone_book[j]):
               return False
           if phone_book[j].startswith(phone_book[i]):
               return False

    return True

# Sorting / Loop를 활용한 solution
def solution_sorting(phone_book):
    # 1. 전화번호 sorting 한다
    phone_book.sort()
    # 2. sorting한 전화번호를 2개씩 확인해서 접두어인지 본다.
    # for i in range(len(phone_book)-1):
    #     if phone_book[i+1].startswith(phone_book[i]):
    #         return False


    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

# Hash를 활용한 solution
def solution(phone_book):
    # 1. Hash map 을 만든다.
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1

    print(hash_map)
    # 2. 접두어가 Hash map 에 존재하는지 찾는다.
    for phone_number in phone_book:
        jubdoo = ''
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다. (기존 번호와 같은 경우는 제외한다)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False

    return True


print(solution(["119", "97674223", "1195524421"])) # false