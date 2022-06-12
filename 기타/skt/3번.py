"""

고객마다 이용하려는 데이터 이상 제공, 이용하려는 부가서비스 모두 포함하는 가장 작은 요금제의 번호 목록
조건을 만족하는 요금제가 없는 경우 0을 담는다.

부가서비스 번호는 중복되어 나타나지 않는다. 오름 차순 정렬

"""


def solution(n, plans, clients):
    answer = []
    basic_service = list(map(int, plans[0].split()))[1:]
    plans[0] = list(map(int, plans[0].split()))
    for i in range(1, len(plans)):
        plan = list(map(int, plans[i].split()))
        for bs in basic_service[::-1]:
            plan.insert(1, bs)
        plans[i] = plan
    for i in range(len(clients)):
        clients[i] = list(map(int, clients[i].split()))
        found = False
        for j in range(len(plans)):
            if clients[i][0] <= plans[j][0]:
                if all(k in plans[j][1:] for k in clients[i][1:]):
                    answer.append(j+1)
                    found = True
                    break
        if not found:
            answer.append(0)


    return answer


# [3,3,1,0]
print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
# [1,2,0]
print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))
