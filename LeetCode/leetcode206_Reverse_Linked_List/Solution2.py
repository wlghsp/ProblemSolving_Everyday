from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Helper functions
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head1 = build_list([1, 2, 3, 4, 5])
    result1 = solution.reverseList(head1)
    print(f"Test 1: {to_array(result1)}")  # Expected: [5, 4, 3, 2, 1]

    # Test case 2
    head2 = build_list([1, 2])
    result2 = solution.reverseList(head2)
    print(f"Test 2: {to_array(result2)}")  # Expected: [2, 1]

    # Test case 3
    head3 = build_list([])
    result3 = solution.reverseList(head3)
    print(f"Test 3: {to_array(result3)}")  # Expected: []

    # Test case 4
    head4 = build_list([1])
    result4 = solution.reverseList(head4)
    print(f"Test 4: {to_array(result4)}")  # Expected: [1]
