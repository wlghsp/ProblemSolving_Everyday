# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


# Helper functions for testing
def create_linked_list(values):
    """리스트를 연결 리스트로 변환"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """연결 리스트를 리스트로 변환"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head1 = create_linked_list([4, 2, 1, 3])
    result1 = solution.sortList(head1)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [1, 2, 3, 4]

    # Test case 2
    head2 = create_linked_list([-1, 5, 3, 4, 0])
    result2 = solution.sortList(head2)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [-1, 0, 3, 4, 5]

    # Test case 3
    head3 = create_linked_list([])
    result3 = solution.sortList(head3)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: []

    # Test case 4
    head4 = create_linked_list([1])
    result4 = solution.sortList(head4)
    print(f"Test 4: {linked_list_to_list(result4)}")  # Expected: [1]
