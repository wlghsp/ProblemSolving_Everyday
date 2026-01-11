# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
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
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseBetween(head1, 2, 4)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [1, 4, 3, 2, 5]

    # Test case 2
    head2 = create_linked_list([5])
    result2 = solution.reverseBetween(head2, 1, 1)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [5]

    # Test case 3
    head3 = create_linked_list([3, 5])
    result3 = solution.reverseBetween(head3, 1, 2)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: [5, 3]

    # Test case 4
    head4 = create_linked_list([1, 2, 3])
    result4 = solution.reverseBetween(head4, 1, 3)
    print(f"Test 4: {linked_list_to_list(result4)}")  # Expected: [3, 2, 1]
