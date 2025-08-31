

def solve(emotions, orders):
    N = len(emotions)

    initial_emotions = emotions[:]
    current_state = emotions.copy()
    is_dead = [False] * N
    result = []

    for i in range(len(orders)):
        water_give_idx = orders[i] - 1
        for j in range(N):
            if is_dead[j]: continue

            if water_give_idx == j:
                current_state[j] = initial_emotions[j]

            current_state[j] -= 1
            if current_state[j] == 0:
                is_dead[j] = True

        cnt = 0
        for state in current_state:
            if state > 0:
               cnt += 1

        result.append(cnt)


    return result



print(solve([2, 3, 1, 2], [3, 1, 2, 1, 4, 1])) #  [4, 2, 2, 2, 2, 1]

