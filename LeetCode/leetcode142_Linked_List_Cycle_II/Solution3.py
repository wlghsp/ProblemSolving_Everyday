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
    s = Solution()

    # Example 1: 3->2->0->-4 (cycle at index 1) -> node with val 2
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # cycle at index 1
    result = s.detectCycle(head)
    print(result.val if result else None)  # Expected: 2

    # Example 2: 1->2 (cycle at index 0) -> node with val 1
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = head2  # cycle at index 0
    result2 = s.detectCycle(head2)
    print(result2.val if result2 else None)  # Expected: 1

    # Example 3: no cycle -> None
    head3 = ListNode(1)
    result3 = s.detectCycle(head3)
    print(result3)  # Expected: None
