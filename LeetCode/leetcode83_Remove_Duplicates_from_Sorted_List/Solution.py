# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        if head.next and head.val == head.next.val:
            return head.next

        return head
    
    def deleteDuplicates_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        LeetCode 83. Remove Duplicates from Sorted List

        정렬된 연결 리스트에서 중복된 값을 제거
        각 값이 한 번씩만 나타나도록 함

        시간복잡도: O(n) - 리스트를 한 번 순회
        공간복잡도: O(1) - 추가 공간 사용 없음

        반복문: 앞에서 뒤로 순차적으로 처리 →→→
        재귀: 끝까지 갔다가 돌아오면서 처리 ↓↓↓ ↑↑↑
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# 헬퍼 함수: 리스트 생성
def create_linked_list(values):
    """리스트에서 연결 리스트 생성"""
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
    """연결 리스트를 리스트 형태로 출력"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    # 테스트 1: [1,1,2]
    print("테스트 1:")
    head1 = create_linked_list([1, 1, 2])
    print(f"입력: {print_linked_list(head1)}")
    result1 = solution.deleteDuplicates(head1)
    print(f"결과: {print_linked_list(result1)}")
    print(f"예상: [1, 2]\n")

    # 테스트 2: [1,1,2,3,3]
    print("테스트 2:")
    head2 = create_linked_list([1, 1, 2, 3, 3])
    print(f"입력: {print_linked_list(head2)}")
    result2 = solution.deleteDuplicates(head2)
    print(f"결과: {print_linked_list(result2)}")
    print(f"예상: [1, 2, 3]\n")

    # 테스트 3: [] (빈 리스트)
    print("테스트 3:")
    head3 = create_linked_list([])
    print(f"입력: {print_linked_list(head3)}")
    result3 = solution.deleteDuplicates(head3)
    print(f"결과: {print_linked_list(result3)}")
    print(f"예상: []\n")

    # 테스트 4: [1] (단일 노드)
    print("테스트 4:")
    head4 = create_linked_list([1])
    print(f"입력: {print_linked_list(head4)}")
    result4 = solution.deleteDuplicates(head4)
    print(f"결과: {print_linked_list(result4)}")
    print(f"예상: [1]\n")

    # 테스트 5: [1,1,1,1,1] (모두 중복)
    print("테스트 5:")
    head5 = create_linked_list([1, 1, 1, 1, 1])
    print(f"입력: {print_linked_list(head5)}")
    result5 = solution.deleteDuplicates(head5)
    print(f"결과: {print_linked_list(result5)}")
    print(f"예상: [1]\n")

    # 테스트 6: [1,2,3] (중복 없음)
    print("테스트 6:")
    head6 = create_linked_list([1, 2, 3])
    print(f"입력: {print_linked_list(head6)}")
    result6 = solution.deleteDuplicates(head6)
    print(f"결과: {print_linked_list(result6)}")
    print(f"예상: [1, 2, 3]\n")
