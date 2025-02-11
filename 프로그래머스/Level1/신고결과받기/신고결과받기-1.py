def solution(id_list, report, k):
    N = len(id_list)
    I = {name: idx for name, idx in zip(id_list, range(len(id_list)))}
    record = [[0] * N for _ in range(N)]
    reported = [0] * N
    report_set = set(report) # 중복 신고 처리

    for r in report_set:
        a, b = r.split()
        reported[I[b]] += 1 # 신고 받음
        record[I[a]][I[b]] += 1 # [a][b] a가 b를 신고

    mail_receive = [0] * N
    for i in range(len(reported)):
        if reported[i] >= k: # i의 신고횟수가 k 이상
            for j in range(N):
                mail_receive[j] += (record[j][i] > 0)

    return mail_receive


print(solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
)) # [0,0]

print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
)) # [2,1,1,0]