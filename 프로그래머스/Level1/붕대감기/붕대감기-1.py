def solution(bandage, health, attacks):
    cur_health = health
    end_time = attacks[len(attacks) - 1][0] # 종료시간

    time = 0
    attack_idx = 0
    success_time = 0
    dead = False
    while time <= end_time:
        if time == attacks[attack_idx][0]: # 공격 당함
            cur_health -= attacks[attack_idx][1]
            if cur_health <= 0: # 죽은 상태
                dead = True
                break
            success_time = 0
            attack_idx += 1
        else: # 붕대 감기
            success_time += 1
            cur_health += bandage[1]

            if success_time == bandage[0]: # 연속성공시간 달성
                success_time = 0
                cur_health += bandage[2]

            if cur_health > health: # 최대 체력을 넘은 경우 최대 체력으로 할당
                cur_health = health

        time += 1

    return -1 if dead else cur_health


print(solution(
    [5, 1, 5], # [시전 시간, 초당 회복량, 추가 회복량]
    30,
    [[2, 10], [9, 15], [10, 5], [11, 5]] # [공격 시간, 피해량]
)) # 5
print(solution(
    [3, 2, 7], # [시전 시간, 초당 회복량, 추가 회복량]
    20,
    [[1, 15], [5, 16], [8, 6]] # [공격 시간, 피해량]
)) # -1
print(solution(
    [4, 2, 7], # [시전 시간, 초당 회복량, 추가 회복량]
    20,
    [[1, 15], [5, 16], [8, 6]] # [공격 시간, 피해량]
)) # -1
print(solution(
    [1, 1, 1], # [시전 시간, 초당 회복량, 추가 회복량]
    5,
    [[1, 2], [3, 2]] # [공격 시간, 피해량]
)) # 3