# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        LeetCode 19. Remove Nth Node From End of List

        연결 리스트의 끝에서 n번째 노드를 제거하고 헤드를 반환

        시간복잡도: O(L) - L: 리스트 길이 (한 번의 순회)
        공간복잡도: O(1) - 추가 공간 사용 없음
        """
        pass


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
    return " -> ".join(values) if values else "[]"


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    # 테스트 1: head = [1,2,3,4,5], n = 2
    print("테스트 1:")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"원본: {print_linked_list(head1)}")
    print(f"n = 2 (끝에서 2번째 제거)")
    result1 = solution.removeNthFromEnd(head1, 2)
    print(f"결과: {print_linked_list(result1)}")
    print(f"예상: 1 -> 2 -> 3 -> 5\n")

    # 테스트 2: head = [1], n = 1
    print("테스트 2:")
    head2 = create_linked_list([1])
    print(f"원본: {print_linked_list(head2)}")
    print(f"n = 1 (유일한 노드 제거)")
    result2 = solution.removeNthFromEnd(head2, 1)
    print(f"결과: {print_linked_list(result2)}")
    print(f"예상: []\n")

    # 테스트 3: head = [1,2], n = 1
    print("테스트 3:")
    head3 = create_linked_list([1, 2])
    print(f"원본: {print_linked_list(head3)}")
    print(f"n = 1 (끝 노드 제거)")
    result3 = solution.removeNthFromEnd(head3, 1)
    print(f"결과: {print_linked_list(result3)}")
    print(f"예상: 1\n")

    # 테스트 4: head = [1,2], n = 2
    print("테스트 4:")
    head4 = create_linked_list([1, 2])
    print(f"원본: {print_linked_list(head4)}")
    print(f"n = 2 (첫 노드 제거)")
    result4 = solution.removeNthFromEnd(head4, 2)
    print(f"결과: {print_linked_list(result4)}")
    print(f"예상: 2\n")

    # 테스트 5: head = [1,2,3,4,5,6,7], n = 4
    print("테스트 5:")
    head5 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    print(f"원본: {print_linked_list(head5)}")
    print(f"n = 4 (끝에서 4번째 제거)")
    result5 = solution.removeNthFromEnd(head5, 4)
    print(f"결과: {print_linked_list(result5)}")
    print(f"예상: 1 -> 2 -> 3 -> 5 -> 6 -> 7\n")
