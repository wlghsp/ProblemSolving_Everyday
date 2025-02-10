from collections import Counter

def solution(participant, completion):
    participant_dict = Counter(participant)
    for c in completion:
        participant_dict[c] -= 1

    # next() 로 특정 조건을 만족하는 첫 번째 요소 가져올 수 있음
    return next(name for name, count in participant_dict.items() if count > 0)



print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # "mislav"