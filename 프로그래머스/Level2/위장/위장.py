


def solution(clothes):
        # 1 옷을 종류별로 구분하기
        hash_map = {}
        for clothe, type in clothes:
            hash_map[type] = hash_map.get(type, 0) + 1

        print(hash_map)
        # 2. 입지 않는 경우를 추가하여 모든 조합을 계산한다.
        answer = 1
        for type in hash_map:
            answer *= (hash_map[type] + 1)

        print(answer)
        # 3. 아무 종류의 옷도 입지 않는 경우를 제외한다.
        return answer-1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))