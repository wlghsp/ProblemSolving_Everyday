from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    # Test 1: [3,2,0,-4], pos=1 (tail connects to index 1) -> True
    a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    a.next = b; b.next = c; c.next = d; d.next = b
    print(Solution().hasCycle(a))   # True

    # Test 2: [1,2], pos=0 -> True
    a, b = ListNode(1), ListNode(2)
    a.next = b; b.next = a
    print(Solution().hasCycle(a))   # True

    # Test 3: [1], pos=-1 -> False
    print(Solution().hasCycle(ListNode(1)))  # False
