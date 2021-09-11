"""
불량이용자 신고 후 처리결과 메일 발송 시스템


1. 각 유저는 한 번에 한 명의 유저 신고 가능
 - 신고횟수 제한 없음
 -여러번 신고 가능하나 동일한 유저에 대한 신고횟수는 1회로 처리. 
2. k번 이상 신고된 유저는 즉시 게시판 이용 정지. 
해당 유저를 신고한 모든 유저에게 정지 사실 메일 발송




출력: 
각 유저별로 처리 결과 메일을 받은 횟수 

신고자는 메일을 받는다. 

"""


def solution(id_list, report, k):
    answer = {}
    id_dict = {}
    reported = []
    for id in id_list:
        id_dict[id] = 0
        answer[id] = 0

    set_report = set(report)
    report_set = list(set_report)
    for r in report_set:
        a, b = r.split()
        reported.append([a, b])
        id_dict[b] += 1

    stopped = []
    for key, v in id_dict.items():
        if v >= k:
            stopped.append(key)
    for s in stopped:
        for r in reported:
            if r[1] == s:
                answer[r[0]] += 1
    answer = [v for v in answer.values()]

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

print(solution(id_list, report, k))
