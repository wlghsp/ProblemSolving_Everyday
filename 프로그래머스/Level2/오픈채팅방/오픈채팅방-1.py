def solution(record):
    answer = []
    id_name = {}
    for r in record:
        r = r.split()
        if r[0] in ['Enter', 'Change']:
            id_name[r[1]] = r[2]

    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append(id_name[r[1]] + '님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(id_name[r[1]] + '님이 나갔습니다.')
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]