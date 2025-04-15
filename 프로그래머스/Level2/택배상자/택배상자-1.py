from collections import deque

def solution(order):
    truck = []
    main_belt = deque([i for i in range(1, len(order) + 1)])
    sub_belt = []
    idx = 0

    def can_proceed():
        if (main_belt and main_belt[0] == order[idx]) or (sub_belt and sub_belt[-1] == order[idx]):
            return True
        return False

    while main_belt or can_proceed():
        if main_belt and main_belt[0] == order[idx]:
            truck.append(main_belt.popleft())
            idx += 1
        elif sub_belt and sub_belt[-1] == order[idx]:
            truck.append(sub_belt.pop())
            idx += 1
        else:
            sub_belt.append(main_belt.popleft())

    return len(truck)

print(solution([4, 3, 1, 2, 5])) # 2
print(solution([5, 4, 3, 2, 1])) # 5