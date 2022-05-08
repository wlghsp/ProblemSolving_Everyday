
"""
한 계정이 여러 번 닉네임 변경이 되면 마지막에 변경한 닉네임으로 출력해야 한다.
딕셔너리에 각 계정마다 최종 닉네임을 저장한다.
Key = 유저아이디, value = 닉네임


"""



def solution(record):
    nickname = dict()
    for log in record:
        words = log.split()
        if words[0] in ['Enter', 'Change']:
            nickname[words[1]] = words[2] # 유저아이디, 닉네임

    answer = []
    for log in record:
        words = log.split()
        if words[0] == 'Enter':
            answer.append(f'{nickname[words[1]]}님이 들어왔습니다.')
        elif words[0] == 'Leave':
            answer.append(f'{nickname[words[1]]}님이 나갔습니다.')


    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))