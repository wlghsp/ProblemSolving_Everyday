


def solution(n, lost, reserve):
    # 1. set을 만든다. (전처리를 하여 2번에서 연산을 단순하게 하였다)
    reserve_only = set(reserve) - set(lost) # 진짜 체육복을 빌려줄 수 있는 학생들만 남음
    lost_only = set(lost) - set(reserve)    # 진짜 체육복을 빌려야 하는 학생들만 남음

    # 2. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only: # 있다면 빌려줄 수 있으므로 lost_only에서 삭제함.
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)

    # 3. 전체 학생 수에 lost_only에 남은 학생 수를 빼준다.
    return n - len(lost_only)


n = 5

lost = [2, 4]

reserve = [1,3,5]

print(solution(n, lost, reserve)) # 5