class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [3,2,0,-4], pos = 1 (cycle exists)
    head1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates cycle
    print(sol.hasCycle(head1))  # Expected: True

    # Test 2: [1,2], pos = 0 (cycle exists)
    head2 = ListNode(1)
    node2_2 = ListNode(2)
    head2.next = node2_2
    node2_2.next = head2  # Creates cycle
    print(sol.hasCycle(head2))  # Expected: True

    # Test 3: [1], pos = -1 (no cycle)
    head3 = ListNode(1)
    print(sol.hasCycle(head3))  # Expected: False
