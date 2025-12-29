# Definition for singly-linked list.
from multiprocessing import current_process
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 해시 테이블 
        """
        방문한 노드를 Set에 저장
        이미 방문한 노드를 다시 만나면 사이클 존재
        1. 빈 Set `visited` 생성
        2. 현재 노드부터 시작하여 순회:
        - 현재 노드가 `visited`에 있으면 → 사이클 존재 → `True`
        - 현재 노드를 `visited`에 추가
        - 다음 노드로 이동
        3. `None`에 도달하면 → 사이클 없음 → `False`
        """
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False


    def hasCycle_floyd(self, head: Optional[ListNode]) -> bool:
        """
        LeetCode 141. Linked List Cycle

        연결 리스트에 사이클이 있는지 판별
        사이클: 리스트 내에서 next 포인터를 계속 따라가면 다시 같은 노드에 도달하는 경우

        시간복잡도: O(n) - Floyd's Cycle Detection Algorithm 사용
        공간복잡도: O(1) - 추가 공간 사용 없음
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# 헬퍼 함수: 사이클이 있는 리스트 생성
def create_cycle_list(values, pos):
    """
    values: 노드 값들의 리스트
    pos: 사이클이 시작되는 인덱스 (-1이면 사이클 없음)
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current

    # 사이클 생성
    if pos != -1 and cycle_node:
        current.next = cycle_node

    return head


# 헬퍼 함수: 리스트 출력 (사이클 감지)
def print_linked_list(head, limit=20):
    """사이클을 고려한 출력 (최대 limit개 노드까지만)"""
    values = []
    current = head
    visited = set()
    count = 0

    while current and count < limit:
        if id(current) in visited:
            values.append(f"{current.val}(사이클 감지)")
            break
        visited.add(id(current))
        values.append(str(current.val))
        current = current.next
        count += 1

    if current and count >= limit:
        values.append("...")

    return " -> ".join(values) if values else "None"


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    # 테스트 1: [3,2,0,-4], pos = 1 (사이클 있음)
    print("테스트 1:")
    head1 = create_cycle_list([3, 2, 0, -4], pos=1)
    print(f"리스트: {print_linked_list(head1)}")
    result1 = solution.hasCycle(head1)
    print(f"결과: {result1}")
    print(f"예상: True (pos=1, 값 2에서 사이클 시작)\n")

    # 테스트 2: [1,2], pos = 0 (사이클 있음)
    print("테스트 2:")
    head2 = create_cycle_list([1, 2], pos=0)
    print(f"리스트: {print_linked_list(head2)}")
    result2 = solution.hasCycle(head2)
    print(f"결과: {result2}")
    print(f"예상: True (pos=0, 값 1에서 사이클 시작)\n")

    # 테스트 3: [1], pos = -1 (사이클 없음)
    print("테스트 3:")
    head3 = create_cycle_list([1], pos=-1)
    print(f"리스트: {print_linked_list(head3)}")
    result3 = solution.hasCycle(head3)
    print(f"결과: {result3}")
    print(f"예상: False (사이클 없음)\n")

    # 테스트 4: [], pos = -1 (빈 리스트)
    print("테스트 4:")
    head4 = create_cycle_list([], pos=-1)
    print(f"리스트: {print_linked_list(head4)}")
    result4 = solution.hasCycle(head4)
    print(f"결과: {result4}")
    print(f"예상: False (빈 리스트)\n")

    # 테스트 5: [1,2,3,4,5], pos = 2 (사이클 있음)
    print("테스트 5:")
    head5 = create_cycle_list([1, 2, 3, 4, 5], pos=2)
    print(f"리스트: {print_linked_list(head5)}")
    result5 = solution.hasCycle(head5)
    print(f"결과: {result5}")
    print(f"예상: True (pos=2, 값 3에서 사이클 시작)\n")
