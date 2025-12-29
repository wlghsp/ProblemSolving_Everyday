# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.call_depth = 0  # 재귀 깊이 추적

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 재귀 호출 시작
        self.call_depth += 1
        current_depth = self.call_depth

        # 현재 노드 출력
        if head:
            print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] head.val = {head.val}")
        else:
            print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] head = None")

        # 베이스 케이스: 빈 리스트 or 노드 1개
        if not head or not head.next:
            print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] 베이스 케이스 도달! 반환: {head.val if head else None}")
            self.call_depth -= 1
            return head

        print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] 재귀 호출 전: head={head.val}, head.next={head.next.val if head.next else None}")

        # 나머지를 뒤집기 (재귀)
        new_head = self.reverseList(head.next)

        print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] 재귀 복귀 후:")
        print(f"{'  ' * (current_depth - 1)}  - 현재 head={head.val}")
        print(f"{'  ' * (current_depth - 1)}  - new_head={new_head.val}")
        print(f"{'  ' * (current_depth - 1)}  - head.next={head.next.val if head.next else None}")

        # 현재 노드를 끝에 연결
        print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] 연결 변경: head.next({head.next.val}).next = head({head.val})")
        head.next.next = head

        print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] head({head.val}).next = None으로 설정")
        head.next = None

        print(f"{'  ' * (current_depth - 1)}[호출 {current_depth}] 반환: new_head={new_head.val}")
        self.call_depth -= 1
        return new_head


# 헬퍼 함수: 리스트 생성
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 헬퍼 함수: 리스트 출력
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) if values else "None"


# 테스트 케이스
if __name__ == "__main__":
    print("=" * 60)
    print("테스트 1: [1, 2, 3, 4, 5]")
    print("=" * 60)
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"원본 리스트: {print_linked_list(head1)}\n")

    solution1 = Solution()
    result1 = solution1.reverseList(head1)

    print(f"\n뒤집은 리스트: {print_linked_list(result1)}")
    print("\n" + "=" * 60 + "\n")

    print("=" * 60)
    print("테스트 2: [1, 2]")
    print("=" * 60)
    head2 = create_linked_list([1, 2])
    print(f"원본 리스트: {print_linked_list(head2)}\n")

    solution2 = Solution()
    result2 = solution2.reverseList(head2)

    print(f"\n뒤집은 리스트: {print_linked_list(result2)}")
    print("\n" + "=" * 60 + "\n")

    print("=" * 60)
    print("테스트 3: [1]")
    print("=" * 60)
    head3 = create_linked_list([1])
    print(f"원본 리스트: {print_linked_list(head3)}\n")

    solution3 = Solution()
    result3 = solution3.reverseList(head3)

    print(f"\n뒤집은 리스트: {print_linked_list(result3)}")
    print("\n" + "=" * 60)
