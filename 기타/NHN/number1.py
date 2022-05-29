from collections import defaultdict

def unique(list):
    return len(list) == len(set(list))

def check(c1, c2):
    return len(list(set(c1).intersection(c2))) == 0

def solution(cards1, cards2):
    answer = 0
    list3 = list(map(list.__add__, cards1, cards2))
    dictionary = defaultdict(int)
    idx = 0
    for round in list3:
        if not unique(round):
            dictionary[idx] = 1
        idx += 1

    idx = 1
    for i in range(1, len(cards1)):
        if not check(cards1[i-1], cards1[i]):
            if dictionary[idx] == 0:
                dictionary[idx] = 1
        idx += 1
    idx = 1
    for i in range(1, len(cards2)):
        if not check(cards2[i-1], cards2[i]):
            if dictionary[idx] == 0:
                dictionary[idx] = 1
        idx += 1
    for k in dictionary.keys():
        if dictionary[k] == 1:
            answer += 1
    return answer



# 플레이어 1이 각 라운드마다 받은 카드들을 의미하는 2차원 정수 배열
cards1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# 플레이어 2가 각 라운드마다 받은 카드들을 의미하는 2차원 정수 배열
cards2 = [[5, 7, 9, 11, 13], [11, 13, 15, 17, 19]]
cards3 = [[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]
cards4 = [[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]
print(solution(cards1, cards2)) # 2
print(solution(cards3, cards4)) # 3