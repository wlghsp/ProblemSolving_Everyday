from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow



if __name__ == "__main__":
    # Test 1: [3,2,0,-4], pos=1 -> node with val=2
    a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    a.next = b; b.next = c; c.next = d; d.next = b
    result = Solution().detectCycle(a)
    print(result.val if result else None)  # 2

    # Test 2: [1,2], pos=0 -> node with val=1
    a, b = ListNode(1), ListNode(2)
    a.next = b; b.next = a
    result = Solution().detectCycle(a)
    print(result.val if result else None)  # 1

    # Test 3: [1], pos=-1 -> None
    result = Solution().detectCycle(ListNode(1))
    print(result.val if result else None)  # None
