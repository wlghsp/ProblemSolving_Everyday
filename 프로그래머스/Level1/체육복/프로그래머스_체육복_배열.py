


def solution(n, lost, reserve):
    # 1. student 배열 생성
    student = [0 for _ in range(n+2)]
    # 2. reserve/lost 정보 반영
    for i in reserve:
        student[i]+= 1
    for i in lost:
        student[i] -= 1

    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n+1):
        if student[i] > 0:
            front = i-1
            back = i + 1
            if student[front] < 0:
                student[front] += 1
                student[i] -= 1
            elif student[back] < 0:
                student[back] += 1
                student[i] -= 1

    # 4. 체육복을 갖고 있는 학생 수를 계산한다.
    answer = 0
    for i in range(1, n+1):
        if student[i] >= 0:
            answer+= 1
    return answer


n = 5

lost = [2, 4]

reserve = [1,3,5]

print(solution(n, lost, reserve)) # 5