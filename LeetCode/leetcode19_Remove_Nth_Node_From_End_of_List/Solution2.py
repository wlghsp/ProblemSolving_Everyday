from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummy.next


# Helper functions
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Remove 2nd from end
    head1 = build_list([1, 2, 3, 4, 5])
    print(to_array(sol.removeNthFromEnd(head1, 2)))  # Expected: [1, 2, 3, 5]

    # Test 2: Single node, remove it
    head2 = build_list([1])
    print(to_array(sol.removeNthFromEnd(head2, 1)))  # Expected: []

    # Test 3: Two nodes, remove first from end
    head3 = build_list([1, 2])
    print(to_array(sol.removeNthFromEnd(head3, 1)))  # Expected: [1]

    # Test 4: Two nodes, remove head
    head4 = build_list([1, 2])
    print(to_array(sol.removeNthFromEnd(head4, 2)))  # Expected: [2]
